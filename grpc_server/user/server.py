from concurrent import futures
import time
import logging
import grpc
import user_pb2
import user_pb2_grpc
import jwt
import traceback

from database.config import engine
from sqlalchemy import insert, text, values, select, update, delete, desc

from model.user import User


class UserService(user_pb2_grpc.UserServiceServicer):
    def list(self, request, context):
        try:
            with engine.connect() as conn:
                result = conn.execute(select(User).order_by(desc(User.id)))
                users = []
                for row in result:
                    users.append(
                        user_pb2.User(
                            id=row[0],
                            name=row[1],
                            email=row[2],
                            password=row[3],
                            role_id=row[4],
                        )
                    )
                return user_pb2.UserListResponse(user=users)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return user_pb2.UserListResponse()

    def get(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(select(User).where(User.id == request.id)).first()
                db.commit()
                if response is None:
                    return user_pb2.UserDetailResponse(user=None)
                return user_pb2.UserDetailResponse(
                    user=user_pb2.User(
                        id=response[0],
                        name=response[1],
                        email=response[2],
                        password=response[3],
                        role_id=response[4],
                    )
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return user_pb2.UserResponse()

    def create(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(
                    insert(User).values(
                        name=request.name,
                        email=request.email,
                        password=request.password,
                        role_id=request.role_id,
                    )
                )
                db.commit()
                if response is None:
                    return user_pb2.UserCreateResponse(user=None)
                return user_pb2.UserCreateResponse(
                    user=user_pb2.User(
                        id=response.inserted_primary_key_rows[0][0],
                        name=request.name,
                        email=request.email,
                        password=request.password,
                        role_id=request.role_id,
                    )
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return user_pb2.UserCreateResponse()

    def update(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(
                    update(User)
                    .where(User.id == request.id)
                    .values(
                        name=request.name,
                        email=request.email,
                        password=request.password,
                        role_id=request.role_id,
                    )
                )
                db.commit()
                if response is None:
                    return user_pb2.UserUpdateResponse(user=None)
                return user_pb2.UserUpdateResponse(
                    user=user_pb2.User(
                        id=request.id,
                        name=request.name,
                        email=request.email,
                        password=request.password,
                        role_id=request.role_id,
                    )
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return user_pb2.UserUpdateResponse()

    def delete(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(delete(User).where(User.id == request.id))
                db.commit()
                if response is None:
                    return user_pb2.UserDeleteResponse()
                return user_pb2.UserDeleteResponse(message="User Deleted")
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return user_pb2.UserDeleteResponse()

    def login(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                res = db.execute(
                    select(User).where(User.email == request.email)
                ).first()
                if res is None:
                    return None
                if res[3] != request.password:
                    return None
                token = jwt.encode(
                    {"id": res[0], "email": res[2]},
                    "secret",
                    algorithm="HS256",
                )
                db.execute(
                    update(User).where(User.email == request.email).values(token=token)
                )
                db.commit()
                res = db.execute(
                    select(User).where(User.email == request.email)
                ).first()
                return user_pb2.UserLoginResponse(token=token)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return None

    def logout(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                token = jwt.decode(request.token, "secret", algorithms=["HS256"])
                db.execute(
                    update(User).where(User.email == token["email"]).values(token="")
                )
                db.commit()
                return user_pb2.UserLogoutResponse(message="Success Logout")
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return None

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port("localhost:5011")
    server.start()
    print("Server started, listening on 5011")
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()