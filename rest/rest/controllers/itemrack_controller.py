from pyramid.view import view_config, view_defaults
from pyramid.response import Response
import grpc

from rest.grpc_client.itemrack.itemrack_client import ItemRackClient


@view_defaults(route_name="RITEM", renderer="json")
class ItemRackController:
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET")
    def get(self):
        try:
            if self.request.params.get("id") is not None:
                id = self.request.params.get("id")
                itemrack = ItemRackClient().get_itemrack(int(id))

                if itemrack == None:
                    return Response(
                        status=404,
                        json_body={"message": "Itemrack not found"},
                    )
                return itemrack

            itemracks = ItemRackClient().list_itemrack()
            return itemracks

        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )

    @view_config(request_method="POST")
    def create(self):
        try:
            if (
                "itemId" not in self.request.json_body
                or "rackId" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={"message": "Missing itemId or rackId"},
                )
            itemId = self.request.json_body["itemId"]
            rackId = self.request.json_body["rackId"]
            itemrack = ItemRackClient().crete_itemrack(int(itemId), int(rackId))

            if itemrack == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to create itemrack"},
                )

            return itemrack
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
            itemrack = ItemRackClient().delete_itemrack(int(id))

            if itemrack == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to delete itemrack"},
                )

            return itemrack
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
                or "itemId" not in self.request.json_body
                or "rackId" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={"message": "Missing id or itemId or rackId"},
                )
            id = self.request.json_body["id"]
            itemId = self.request.json_body["itemId"]
            rackId = self.request.json_body["rackId"]
            itemrack = ItemRackClient().update_itemrack(
                int(id), int(itemId), int(rackId)
            )

            if itemrack == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to update itemrack"},
                )

            return itemrack
        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )
    
    @view_config(route_name="getItemByRackId", request_method="GET")
    def getItemByRackId(self):
        try:
            if self.request.params.get("rackId") is None:
                return Response(
                    status=400,
                    json_body={"message": "Missing id"},
                )
            id = self.request.params.get("rackId")
            itemrack = ItemRackClient().getItemByRackId(int(id))

            if itemrack == None:
                return Response(
                    status=404,
                    json_body={"message": "Itemrack not found"},
                )
            return itemrack
        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )
        
