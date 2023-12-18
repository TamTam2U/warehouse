import rest.grpc_client.user.user_pb2_grpc as user_pb2_grpc
import rest.grpc_client.user.user_pb2 as user_pb2
import grpc
import traceback

from rest.grpc_client.role.role_client import RoleClient

class UserClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 5011

        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")
        self.stub = user_pb2_grpc.UserServiceStub(self.channel)

    def list_user(self):
        try:
            res = self.stub.list(user_pb2.UserListRequest())

            if len(res.user) == 0:
                return None
            
            roleClient = RoleClient()

            return [
                dict(
                    id=user.id,
                    name=user.name,
                    email=user.email,
                    password=user.password,
                    role_id=user.role_id,
                    token=user.token,
                    role=roleClient.get_role(user.role_id),
                )
                for user in res.user
            ]

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            return None

    def get_user(self, id):
        try:
            res = self.stub.get(user_pb2.UserDetailRequest(id=int(id)))

            if res is None:
                return None
            
            roleClient = RoleClient()
    
            return dict(
                id=res.user.id,
                name=res.user.name,
                email=res.user.email,
                password=res.user.password,
                role_id=res.user.role_id,
                token=res.user.token,
                role=roleClient.get_role(res.user.role_id)
            )

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            return None

    def create_user(self, name, email, role_id):
        try:
            res = self.stub.create(
                user_pb2.UserCreateRequest(
                    name=name, email=email, password="password", role_id=int(role_id)
                )
            )

            if res is None:
                return None

            roleClient = RoleClient()
            
            return dict(
                id=res.user.id,
                name=res.user.name,
                email=res.user.email,
                password=res.user.password,
                role_id=res.user.role_id,
                token=res.user.token,
                role=roleClient.get_role(res.user.role_id),
            )

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            return None

    def update_user(self, id, name, email, role_id):
        try:
            res = self.stub.update(
                user_pb2.UserUpdateRequest(
                    id=int(id),
                    name=name,
                    email=email,
                    password="password",
                    role_id=int(role_id),
                )
            )

            if res is None:
                return None
            
            roleClient = RoleClient()

            return dict(
                id=res.user.id,
                name=res.user.name,
                email=res.user.email,
                password=res.user.password,
                role_id=res.user.role_id,
                token=res.user.token,
                role=roleClient.get_role(res.user.role_id),
            )

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            return None

    def delete_user(self, id):
        try:
            res = self.stub.delete(user_pb2.UserDeleteRequest(id=int(id)))

            if res is None:
                return None

            return dict(message="success deleted")

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            return None

    def login(self, email, password):
        try:
            res = self.stub.login(
                user_pb2.UserLoginRequest(email=email, password=password)
            )

            if res is None:
                return None

            return dict(
                token=res.token,
            )

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            return None

    def logout(self, token):
        try:
            res = self.stub.logout(user_pb2.UserLogoutRequest(token=token))

            if res is None:
                return None

            return dict(message="success logout")

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            return None

# if __name__ == "__main__":
#     while True:
#         print("1. list user")
#         print("2. get user")
#         print("3. create user")
#         print("4. update user")
#         print("5. delete user")
#         print("6. login")
#         print("7. logout")
#         print("8. exit")

#         choice = input("Enter your choice: ")
#         client = UserClient()

#         if choice == "1":
#             res = client.list_user()
#             print(res)
#         elif choice == "2":
#             id = input("Enter user id: ")
#             res = client.get_user(id)
#             print(res)
#         elif choice == "3":
#             name = input("Enter user name: ")
#             email = input("Enter user email: ")
#             role_id = input("Enter user role id: ")
#             res = client.create_user(name, email, role_id)
#             print(res)
#         elif choice == "4":
#             id = input("Enter user id: ")
#             name = input("Enter user name: ")
#             email = input("Enter user email: ")
#             role_id = input("Enter user role id: ")
#             res = client.update_user(id, name, email, role_id)
#             print(res)
#         elif choice == "5":
#             id = input("Enter user id: ")
#             res = client.delete_user(id)
#             print(res)
#         elif choice == "6":
#             email = input("Enter user email: ")
#             password = input("Enter user password: ")
#             res = client.login(email, password)
#             print(res)
#         elif choice == "7":
#             token = input("Enter user token: ")
#             res = client.logout(token)
#             print(res)
#         elif choice == "8":
#             break
