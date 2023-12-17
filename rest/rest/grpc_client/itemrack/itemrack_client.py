import rest.grpc_client.itemrack.itemrack_pb2_grpc as itemrack_pb2_grpc
import rest.grpc_client.itemrack.itemrack_pb2 as itemrack_pb2
import grpc

from rest.grpc_client.item.item_client import ItemClient
from rest.grpc_client.rack.rack_client import RackClient


class ItemRackClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 5006

        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")
        self.stub = itemrack_pb2_grpc.ItemRackServiceStub(self.channel)

    def list_itemrack(self):
        res = self.stub.list(itemrack_pb2.ItemRackListRequest())

        if len(res.itemRack) == 0:
            return None

        itemClient = ItemClient()
        rackClient = RackClient()

        return [
            dict(
                id=itemrack.id,
                itemId=itemrack.itemId,
                rackId=itemrack.rackId,
                item=itemClient.get_item(itemrack.itemId),
                rack=rackClient.get_rack(itemrack.rackId),
            )
            for itemrack in res.itemRack
        ]

    def get_itemrack(self, id):
        res = self.stub.get(itemrack_pb2.ItemRackDetailRequest(id=int(id)))

        if res is None:
            return None

        itemClient = ItemClient()
        rackClient = RackClient()

        return dict(
            id=res.itemRack.id,
            itemId=res.itemRack.itemId,
            rackId=res.itemRack.rackId,
            item=itemClient.get_item(res.itemrack.itemId),
            rack=rackClient.get_rack(res.itemrack.rackId),
        )

    def crete_itemrack(self, itemId, rackId):
        res = self.stub.create(
            itemrack_pb2.ItemRackCreateRequest(itemId=int(itemId), rackId=int(rackId))
        )

        if res is None:
            return None

        itemClient = ItemClient()
        rackClient = RackClient()

        return dict(
            id=res.itemRack.id,
            itemId=res.itemRack.itemId,
            rackId=res.itemRack.rackId,
            item=itemClient.get_item(res.itemRack.itemId),
            rack=rackClient.get_rack(res.itemRack.rackId),
        )

    def update_itemrack(self, id, itemId, rackId):
        res = self.stub.update(
            itemrack_pb2.ItemRackUpdateRequest(
                id=id, itemId=int(itemId), rackId=int(rackId)
            )
        )

        if res is None:
            return None

        itemClient = ItemClient()
        rackClient = RackClient()

        return dict(
            id=res.itemRack.id,
            itemId=res.itemRack.itemId,
            rackId=res.itemRack.rackId,
            item=itemClient.get_item(res.itemRack.itemId),
            rack=rackClient.get_rack(res.itemRack.rackId),
        )

    def delete_itemrack(self, id):
        res = self.stub.delete(itemrack_pb2.ItemRackDeleteRequest(id=int(id)))

        if res is None:
            return None

        return dict(message="success deleted")
