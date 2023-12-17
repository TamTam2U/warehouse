import rack_pb2_grpc as rack_pb2_grpc
import rack_pb2 as rack_pb2
import grpc
import traceback


class RackClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 5008

        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")
        self.stub = rack_pb2_grpc.RackServiceStub(self.channel)

    def list_rack(self):
        response = self.stub.list(rack_pb2.RackListRequest())

        if len(response.rack) == 0:
            return None

        return [dict(id=rack.id, name=rack.name) for rack in response.rack]

    def get_rack(self, id):
        response = self.stub.get(rack_pb2.RackDetailRequest(id=int(id)))

        if response.rack is None:
            return None

        return dict(id=response.rack.id, name=response.rack.name)

    def create_rack(self, name):
        response = self.stub.create(rack_pb2.RackCreateRequest(name=name))

        if response.rack is None:
            return None

        return dict(id=response.rack.id, name=response.rack.name)

    def update_rack(self, id, name):
        response = self.stub.update(rack_pb2.RackUpdateRequest(id=int(id), name=name))

        if response.rack is None:
            return None

        return dict(id=response.rack.id, name=response.rack.name)

    def delete_rack(self, id):
        response = self.stub.delete(rack_pb2.RackDeleteRequest(id=int(id)))

        return dict(message="Rack deleted successfully")


if __name__ == "__main__":
    while True:
        print("1. List Racks")
        print("2. Get Rack")
        print("3. Create Rack")
        print("4. Update Rack")
        print("5. Delete Rack")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            rack_client = RackClient()
            racks = rack_client.list_rack()
            print(racks)
        elif choice == "2":
            rack_id = input("Enter the rack id: ")
            rack_client = RackClient()
            rack = rack_client.get_rack(rack_id)
            print(rack)
        elif choice == "3":
            rack_name = input("Enter the rack name: ")
            rack_client = RackClient()
            rack = rack_client.create_rack(rack_name)
            print(rack)
        elif choice == "4":
            rack_id = input("Enter the rack id: ")
            rack_name = input("Enter the rack name: ")
            rack_client = RackClient()
            rack = rack_client.update_rack(rack_id, rack_name)
            print(rack)
        elif choice == "5":
            rack_id = input("Enter the rack id: ")
            rack_client = RackClient()
            rack = rack_client.delete_rack(rack_id)
            print(rack)
        elif choice == "6":
            break
        else:
            print("Invalid choice")
