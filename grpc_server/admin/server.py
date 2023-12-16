from concurrent import futures
import time
import logging
import grpc
import admin_pb2
import admin_pb2_grpc
import traceback
import jwt

from database.config import engine
from sqlalchemy import insert, text, values, select, update, delete, desc

from model.admin import Admin


class AdminService(admin_pb2_grpc.AdminServiceServicer):
    def list(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(select(Admin).order_by(desc(Admin.id)))
                admin = []
                for row in response:
                    admin.append(
                        admin_pb2.Admin(
                            id=row[0],
                            email=row[1],
                            password=row[2],
                            otp=row[3],
                            token=row[4],
                        )
                    )
                return admin_pb2.AdminListResponse(admin=admin)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return admin_pb2.AdminListResponse()

    def get(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(
                    select(Admin).where(Admin.id == request.id)
                ).first()

                db.commit()

                if response is None:
                    return admin_pb2.AdminResponse(admin=None)

                return admin_pb2.AdminResponse(
                    admin=admin_pb2.Admin(
                        id=response[0],
                        email=response[1],
                        password=response[2],
                        otp=response[3],
                        token=response[4],
                    )
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return admin_pb2.AdminListResponse()

    def create(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(
                    insert(Admin).values(email=request.email, password=request.password)
                )
                db.commit()

                if response is None:
                    context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                    return admin_pb2.AdminCreateResponse(admin=None)

                return admin_pb2.AdminCreateResponse(
                    admin=admin_pb2.Admin(
                        id=response.inserted_primary_key_rows[0][0],
                        email=request.email,
                        password=request.password,
                        # otp="",
                        # token="",
                    )
                )

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return admin_pb2.AdminCreateResponse()

    def update(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(
                    update(Admin)
                    .where(Admin.id == request.id)
                    .values(email=request.email, password=request.password)
                )
                db.commit()

                if response is None:
                    context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                    return admin_pb2.AdminUpdateResponse(admin=None)

                return admin_pb2.AdminUpdateResponse(
                    admin=admin_pb2.Admin(
                        id=request.id,
                        email=request.email,
                        password=request.password,
                        # otp="",
                        # token="",
                    )
                )

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return admin_pb2.AdminUpdateResponse()

    def delete(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(delete(Admin).where(Admin.id == request.id))
                db.commit()

                if response is None:
                    context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                    return admin_pb2.AdminDeleteResponse()

                return admin_pb2.AdminDeleteResponse(
                    message="Success Deleted",
                )

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return admin_pb2.AdminDeleteResponse()

    def login(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                res = db.execute(
                    select(Admin).where(Admin.email == request.email)
                ).first()

                db.commit()

                if res is None:
                    return None

                if res[2] != request.password:
                    return None

                token = jwt.encode(
                    {"id": res[0], "email": res[1]},
                    "secret",
                    algorithm="HS256",
                )

                db.execute(
                    update(Admin)
                    .where(Admin.email == request.email)
                    .values(token=token)
                )

                res = db.execute(
                    select(Admin).where(Admin.email == request.email)
                ).first()

                db.commit()

                return admin_pb2.AdminLoginResponse(
                    id=res[0], email=res[1], token=token
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return None


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    admin_pb2_grpc.add_AdminServiceServicer_to_server(AdminService(), server)
    server.add_insecure_port("localhost:5002")
    server.start()
    print("Server started, listening on 5002")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
