import role_pb2_grpc as role_pb2_grpc
import role_pb2 as role_pb2
import grpc

class RoleClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 5009
        
        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")
        self.stub = role_pb2_grpc.RoleServiceStub(self.channel)
    
    def list_role(self):
        request = role_pb2.RoleListRequest()
        response = self.stub.list(request)
        
        if len(response.role) == 0:
            return None
        
        return[
            dict(
                id = role.id,
                name = role.name
            )
            for role in response.role
        ]
    
    def get_role(self,id):
        request = role_pb2.RoleDetailRequest(id=int(id))
        response = self.stub.get(request)
        
        if response.role is None:
            return None
        
        return dict(
            id = response.role.id,
            name = response.role.name
        )
    
    def create_role(self,name):
        request = role_pb2.RoleCreateRequest(name=name)
        response = self.stub.create(request)
        
        if response.role is None:
            return None
        
        return dict(
            id = response.role.id,
            name = response.role.name
        )
    
    def update_role(self,id,name):
        request = role_pb2.RoleUpdateRequest(id=int(id),name=name)
        response = self.stub.update(request)
        
        if response.role is None:
            return None
        
        return dict(
            id = response.role.id,
            name = response.role.name
        )
    
    def delete_role(self,id):
        request = role_pb2.RoleDeleteRequest(id=int(id))
        response = self.stub.delete(request)
        
        if response is None:
            return None
        
        return dict(
            message = "Role deleted successfully"
        )

if __name__ == "__main__":
    while True:
        print("1. list role")
        print("2. get role")
        print("3. create role")
        print("4. update role")
        print("5. delete role")
        print("6. exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(RoleClient().list_role())
        elif choice == 2:
            id = int(input("Enter role id: "))
            print(RoleClient().get_role(id))
        elif choice == 3:
            name = input("Enter role name: ")
            print(RoleClient().create_role(name))
        elif choice == 4:
            id = int(input("Enter role id: "))
            name = input("Enter role name: ")
            print(RoleClient().update_role(id,name))
        elif choice == 5:
            id = int(input("Enter role id: "))
            print(RoleClient().delete_role(id))
        elif choice == 6:
            break