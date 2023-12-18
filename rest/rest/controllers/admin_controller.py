from pyramid.view import view_config, view_defaults
from pyramid.response import Response

from rest.grpc_client.admin.admin_client import AdminClient

import grpc


@view_defaults(route_name="admin", renderer="json")
class AdminController:
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET")
    def get(self):
        try:
            if self.request.params.get("id") is not None:
                id = self.request.params.get("id")
                admin = AdminClient().get_admin(int(id))

                if admin == None:
                    return Response(
                        status=404,
                        json_body={"message": "Admin not found"},
                    )
                return admin
            admins = AdminClient().list_admin()
            return admins
        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )

    @view_config(request_method="POST")
    def create(self):
        try:
            if (
                "email" not in self.request.json_body
                or "password" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={"message": "Missing email or password"},
                )
            admin = AdminClient().create_admin(
                self.request.json_body["email"], self.request.json_body["password"]
            )
            if admin == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to create admin"},
                )
            return admin
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
            admin = AdminClient().delete_admin(int(id))
            if admin == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to delete admin"},
                )
            return admin
        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )

    @view_config(route_name="login", request_method="POST")
    def login(self):
        try:
            if (
                "email" not in self.request.json_body
                or "password" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={"message": "Missing email or password"},
                )
            admin = AdminClient().login(
                self.request.json_body["email"], self.request.json_body["password"]
            )
            if admin == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to login admin"},
                )
            return admin

        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )

    @view_config(route_name="logout", request_method="POST")
    def logout(self):
        try:
            if "token" not in self.request.json_body:
                return Response(
                    status=400,
                    json_body={"message": "Missing token"},
                )
            token = self.request.json_body["token"]
            admin = AdminClient().logout(token)
            if admin == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to logout admin"},
                )
            return admin
        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )
