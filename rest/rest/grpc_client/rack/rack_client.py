import rest.grpc_client.rack.rack_pb2_grpc as rack_pb2_grpc
import rest.grpc_client.rack.rack_pb2 as rack_pb2
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



