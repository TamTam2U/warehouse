import item_pb2_grpc as item_pb2_grpc
import item_pb2 as item_pb2
import grpc

class ItemClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 5005

        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")
        self.stub = item_pb2_grpc.ItemServiceStub(self.channel)
    
    def list_item(self):
        request = item_pb2.ItemListRequest()
        response = self.stub.list(request)
        
        if len(response.item) == 0:
            return None
        
        return [
            dict(
                id = item.id,
                name = item.name,
                kategoriId = item.kategoriId
            )
            for item in response.item
        ]
    
    def get_item(self, id):
        request = item_pb2.ItemDetailRequest(id=int(id))
        response = self.stub.detail(request)
        
        if response.item is None:
            return None
        
        return dict(
            id = response.item.id,
            name = response.item.name,
            kategoriId = response.item.kategoriId
        )
    
    def create_item(self, name, kategoriId):
        request = item_pb2.ItemCreateRequest(name=name, kategoriId=kategoriId)
        response = self.stub.create(request)
        
        if response.item is None:
            return None
        
        return dict(
            id = response.item.id,
            name = response.item.name,
            kategoriId = response.item.kategoriId
        )
    
    def update_item(self, id, name):
        request = item_pb2.ItemUpdateRequest(id=int(id), name=name)
        response = self.stub.update(request)
        
        if response.item is None:
            return None
        
        return dict(
            id = response.item.id,
            name = response.item.name,
            message = "Item updated successfully"
        )
    
    def delete_item(self, id):
        request = item_pb2.ItemDeleteRequest(id=int(id))
        response = self.stub.delete(request)
        
        if response is None:
            return None
        
        return dict(
            message = "Item deleted successfully"
        )

if __name__ == "__main__":
    while True:
        print("1. List item")
        print("2. Get item")
        print("3. Create item")
        print("4. Update item")
        print("5. Delete item")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            item = ItemClient().list_item()
            print(item)
        elif choice == 2:
            id = int(input("Enter item id: "))
            item = ItemClient().get_item(id)
            print(item)
        elif choice == 3:
            name = input("Enter item name: ")
            kategoriId = int(input("Enter kategoriId: "))
            item = ItemClient().create_item(name, kategoriId)
            print(item)
        elif choice == 4:
            id = int(input("Enter item id: "))
            name = input("Enter item name: ")
            item = ItemClient().update_item(id, name)
            print(item)
        elif choice == 5:
            id = int(input("Enter item id: "))
            item = ItemClient().delete_item(id)
            print(item)
        elif choice == 6:
            break