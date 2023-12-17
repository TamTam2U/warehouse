import itemrack_pb2_grpc as itemrack_pb2_grpc
import itemrack_pb2 as itemrack_pb2
import grpc

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
        
        return [
            dict(
                id=itemrack.id,
                itemId=itemrack.itemId,
                rackId=itemrack.rackId
            )
            for itemrack in res.itemRack
        ]
    
    def get_itemrack(self, id):
        res = self.stub.get(itemrack_pb2.ItemRackDetailRequest(id=int(id)))
        
        if res is None:
            return None
        
        return dict(
            id=res.itemRack.id,
            itemId=res.itemRack.itemId,
            rackId=res.itemRack.rackId
        )
    
    def crete_itemrack(self,itemId,rackId):
        res = self.stub.create(itemrack_pb2.ItemRackCreateRequest(itemId=int(itemId),rackId=int(rackId)))
        
        if res is None:
            return None
        
        return dict(
            id=res.itemRack.id,
            itemId=res.itemRack.itemId,
            rackId=res.itemRack.rackId
        )

    def update_itemrack(self, id, itemId, rackId):
        res = self.stub.update(itemrack_pb2.ItemRackUpdateRequest(id=id,itemId=int(itemId),rackId=int(rackId)))
        
        if res is None:
            return None
        
        return dict(
            id=res.itemRack.id,
            itemId=res.itemRack.itemId,
            rackId=res.itemRack.rackId
        )

    def delete_itemrack(self, id):
        res = self.stub.delete(itemrack_pb2.ItemRackDeleteRequest(id=int(id)))
        
        if res is None:
            return None
        
        return dict(
            message="success deleted"
        )

if __name__ == "__main__":
    while True:
        print("ItemRack Client")
        print("1. List ItemRack")
        print("2. Get ItemRack")
        print("3. Create ItemRack")
        print("4. Update ItemRack")
        print("5. Delete ItemRack")
        print("0. Exit")
        choice = input("Enter your choice: ")

        itemrack = ItemRackClient()

        if choice == "1":
            print(itemrack.list_itemrack())
        elif choice == "2":
            id = int(input("Enter id: "))
            print(itemrack.get_itemrack(id))

        elif choice == "3":
            itemId = int(input("Enter itemId: "))
            rackId = int(input("Enter rackId: "))
            print(itemrack.crete_itemrack(itemId,rackId))

        elif choice == "4":
            id = int(input("Enter id: "))
            itemId = int(input("Enter itemId: "))
            rackId = int(input("Enter rackId: "))
            print(itemrack.update_itemrack(id,itemId,rackId))

        elif choice == "5":
            id = int(input("Enter id: "))
            print(itemrack.delete_itemrack(id))
        elif choice == "0":
            break