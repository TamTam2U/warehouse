from pyramid.view import view_config, view_defaults
from pyramid.response import Response

from rest.grpc_client.item.item_client import ItemClient
import grpc


@view_defaults(route_name="item", renderer="json")
class ItemController:
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET")
    def get(self):
        try:
            if self.request.params.get("id") is not None:
                id = self.request.params.get("id")
                item = ItemClient().get_item(int(id))

                if item == None:
                    return Response(
                        status=404,
                        json_body={"message": "Item not found"},
                    )
                return item

            items = ItemClient().list_item()
            return items

        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )

    @view_config(request_method="POST")
    def create(self):
        try:
            if (
                "name" not in self.request.json_body
                or "kategoriId" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={"message": "Missing name or kategori"},
                )
                
            client = ItemClient()
            result = client.create_item(
                self.request.json_body["name"], self.request.json_body["kategoriId"]
            )
            
            if result == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to create item"},
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
                
            client = ItemClient()
            result = client.update_item(
                self.request.json_body["id"], self.request.json_body["name"]
            )
            
            if result == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to update item"},
                )

            return result
        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )
