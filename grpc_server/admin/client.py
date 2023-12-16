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
    
    def create_admin(self,email,passwor):
        try:
            res = self.stub.create(admin_pb2.AdminCreateRequest(email=email,password=password))
            
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
    
    def update_admin(self,id,email,password):
        try:
            res = self.stub.update(admin_pb2.AdminUpdateRequest(id=id,email=email,password=password))
            
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
    
    def delete_admin(self,id):
        try:
            res = self.stub.delete(admin_pb2.AdminDeleteRequest(id=id))
            
            if res is None:
                return None
            
            return dict(
                message = "success deleted"
            )
        except Exception as e:
            print(e)
            print(traceback.print_exc())
            return None
    
    def login(self,email,password):
        try:
            res = self.stub.login(admin_pb2.AdminLoginRequest(email=email,password=password))
            
            if res is None:
                return None
            
            return dict(
                id = res.id,
                email = res.email,
                token = res.token
            )
        except Exception as e:
            print(e)
            print(traceback.print_exc())
            return None

if __name__ == "__main__":
    while True:
        print("1. List admin")
        print("2. Get admin")
        print("3. Create admin")
        print("4. Update admin")
        print("5. Delete admin")
        print("6. Login")
        choice = input("Enter your choice: ")
        if choice == "1":
            client = AdminClient()
            print(client.list_admin())
        elif choice == "2":
            client = AdminClient() 
            id = input("Enter id: ")
            print(client.get_admin(int(id)))
        elif choice == "3":
            client = AdminClient()
            email = input("Enter email: ")
            password = input("Enter password: ")
            print(client.create_admin(email,password))
        elif choice == "4":
            client = AdminClient()
            id = input("Enter id: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            print(client.update_admin(int(id),email,password))
        elif choice == "5":
            client = AdminClient()
            id = input("Enter id: ")
            print(client.delete_admin(int(id)))
        elif choice == "6":
            client = AdminClient()
            email = input("Enter email: ")
            password = input("Enter password: ")
            print(client.login(email,password))
        else:
            break