import admin_pb2_grpc as admin_pb2_grpc
import admin_pb2 as admin_pb2
import grpc
import traceback

class AdminClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 5002
        
        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")
        self.stub = admin_pb2_grpc.AdminServiceStub(self.channel)
        
    def list_admin(self):
        try:
            res = self.stub.list(admin_pb2.AdminListRequest())
        
            if len(res.admin) == 0:
                return None
        
            return [
                dict(
                    id = admin.id,
                    email = admin.email,
                    password = admin.password,
                    otp = admin.otp,
                    token = admin.token
                )
                for admin in res.admin
            ]
        except Exception as e:
            traceback.print_exc()
            return None
    
    def get_admin(self,id):
        try:
            res = self.stub.get(admin_pb2.AdminRequest(id=id))
            
            if res is None:
                return None
            
            return dict(
                id = res.admin.id,
                email = res.admin.email,
                password = res.admin.password,
                otp = res.admin.otp,
                token = res.admin.token
            )
            
        except Exception as e:
            print(e)
            print(traceback.print_exc())
            return None
            

if __name__ == "__main__":
    while True:
        print("1. List admin")
        print("2. Get admin")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            client = AdminClient()
            print(client.list_admin())
        elif choice == "2":
            client = AdminClient() 
            id = input("Enter id: ")
            print(client.get_admin(int(id)))
        elif choice == "3":
            break