from pyramid.view import view_config, view_defaults
from pyramid.response import Response

from rest.grpc_client.user.user_client import UserClient

import grpc


@view_defaults(route_name="user", renderer="json")
class UserController:
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET")
    def get(self):
        try:
            if self.request.params.get("id") is not None:
                id = self.request.params.get("id")
                user = UserClient().get_user(int(id))

                if user == None:
                    return Response(
                        status=404,
                        json_body={"message": "User not found"},
                    )
                return user

            users = UserClient().list_user()
            return users

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
            user = UserClient().delete_user(int(id))

            if user == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to delete user"},
                )
            return user
        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )

    @view_config(request_method="POST")
    def create(self):
        try:
            if (
                "name" not in self.request.json_body
                or "email" not in self.request.json_body
                or "role_id" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={"message": "Missing name or email or role_id"},
                )
            name = self.request.json_body["name"]
            email = self.request.json_body["email"]
            role_id = self.request.json_body["role_id"]
            user = UserClient().create_user(name, email, int(role_id))

            if user == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to create user"},
                )
            return user
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
                or "name" not in self.request.json_body
                or "email" not in self.request.json_body
                or "role_id" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={"message": "Missing id or name or email or role_id"},
                )
            id = self.request.json_body["id"]
            name = self.request.json_body["name"]
            email = self.request.json_body["email"]
            role_id = self.request.json_body["role_id"]
            user = UserClient().update_user(int(id), name, email, int(role_id))

            if user == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to update user"},
                )
            return user
        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )

    @view_config(route_name="Ulogin",request_method="POST")
    def login(self):
        try:
            if (
                "email" not in self.request.json_body
                or "password" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={"message": "Missing email or password"},
                )
            email = self.request.json_body["email"]
            password = self.request.json_body["password"]
            user = UserClient().login(email, password)

            if user == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to login user"},
                )
            return user
        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )
    
    @view_config(route_name="Slogout",request_method="POST")
    def logout(self):
        try:
            token = self.request.json_body["token"]
            if token is None:
                return Response(
                    status=400,
                    json_body={"message": "Missing token"},
                )
            user = UserClient().logout(token)
            if user == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to logout user"},
                )
            return user
        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )
    
    
