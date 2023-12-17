from pyramid.view import view_config, view_defaults
from pyramid.response import Response
import grpc

from rest.grpc_client.rack.rack_client import RackClient


@view_defaults(route_name="rack", renderer="json")
class RackController:
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET")
    def get(self):
        try:
            if self.request.params.get("id") is not None:
                id = self.request.params.get("id")
                client = RackClient()
                result = client.get_rack(int(id))
                if result == None:
                    return Response(
                        status=404,
                        json_body={"message": "Rack not found"},
                    )
                return result
            client = RackClient()
            results = client.list_rack()
            if results == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to get rack"},
                )
            return results
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
                    json_body={"message": "Missing name"},
                )
            client = RackClient()
            result = client.create_rack(self.request.json_body["name"])
            if result == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to create rack"},
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
            name = self.request.json_body["name"]
            client = RackClient()
            result = client.update_rack(int(id), name)
            if result == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to update rack"},
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
            client = RackClient()
            result = client.delete_rack(int(id))
            if result == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to delete rack"},
                )
            return result
        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )
