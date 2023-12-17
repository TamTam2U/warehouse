from pyramid.view import view_config, view_defaults
from pyramid.response import Response
import grpc

from rest.grpc_client.role.role_client import RoleClient


@view_defaults(route_name="role", renderer="json")
class RoleController:
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET")
    def get(self):
        try:
            if self.request.params.get("id") is not None:
                id = self.request.params.get("id")
                role = RoleClient().get_role(int(id))

                if role == None:
                    return Response(
                        status=404,
                        json_body={"message": "Role not found"},
                    )
                return role

            roles = RoleClient()
            list = roles.list_role()
            return list
        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )

    @view_config(request_method="POST")
    def create(self):
        try:
            if "name" not in self.request.json_body:
                return Response(
                    status=400,
                    json_body={"message": "Missing role"},
                )

            role = self.request.json_body["name"]
            result = RoleClient().create_role(role)

            if result == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to create role"},
                )

            return result
        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )

    @view_config(request_method="PUT")
    def update(self):
        try:
            if (
                "id" not in self.request.json_body
                or "name" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={"message": "Missing id or name"},
                )

            id = self.request.json_body["id"]
            role = self.request.json_body["name"]
            result = RoleClient().update_role(int(id), role)

            if result == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to update role"},
                )

            return result
        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )

    @view_config(request_method="DELETE")
    def delete(self):
        try:
            if self.request.params.get("id") is None:
                return Response(
                    status=400,
                    json_body={"message": "Missing id"},
                )

            id = self.request.params.get("id")
            result = RoleClient().delete_role(int(id))

            if result == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to delete role"},
                )

            return result
        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )
