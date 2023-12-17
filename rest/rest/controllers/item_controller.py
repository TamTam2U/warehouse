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
            else:
                items = ItemClient().list_item()
                return items

        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )
