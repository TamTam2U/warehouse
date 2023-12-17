from concurrent import futures
import time
import logging
import grpc
import role_pb2
import role_pb2_grpc
import traceback

from database.config import engine
from sqlalchemy import insert, text, values, select, update, delete, desc

from model.role import Role


class RoleService(role_pb2_grpc.RoleServiceServicer):
    def list(self, request, context):
        try:
            with engine.connect() as conn:
                result = conn.execute(select(Role).order_by(desc(Role.id)))
                roles = []
                for row in result:
                    roles.append(
                        role_pb2.Role(
                            id=row[0],
                            name=row[1],
                        )
                    )
                return role_pb2.RoleListResponse(role=roles)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return role_pb2.RoleListResponse()

    def get(self, request, context):
        try:
            with engine.connect() as conn:
                result = conn.execute(select(Role).where(Role.id == request.id)).first()

                conn.commit()

                if result is None:
                    return role_pb2.RoleDetailResponse()

                return role_pb2.RoleDetailResponse(
                    role=role_pb2.Role(
                        id=result[0],
                        name=result[1],
                    )
                )

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return role_pb2.RoleDetailResponse()

    def create(self, request, context):
        try:
            with engine.connect() as conn:
                result = conn.execute(insert(Role).values(name=request.name))
                conn.commit()
                
                if result is None:
                    return role_pb2.RoleCreateResponse()
                
                return role_pb2.RoleCreateResponse(
                    role=role_pb2.Role(
                        id=result.inserted_primary_key_rows[0][0],
                        name=request.name,
                    )
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return role_pb2.RoleCreateResponse()
    
    def update(self, request, context):
        try:
            with engine.connect() as conn:
                result = conn.execute(update(Role).where(Role.id == request.id).values(name=request.name))
                conn.commit()
                
                if result is None:
                    return role_pb2.RoleUpdateResponse()
                
                return role_pb2.RoleUpdateResponse(
                    role=role_pb2.Role(
                        id=request.id,
                        name=request.name,
                    )
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return role_pb2.RoleUpdateResponse()
    
    def delete(self, request, context):
        try:
            with engine.connect() as conn:
                result = conn.execute(delete(Role).where(Role.id == request.id))
                conn.commit()
                
                if result is None:
                    return role_pb2.RoleDeleteResponse()
                
                return role_pb2.RoleDeleteResponse(
                    message="Success"
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return role_pb2.RoleDeleteResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    role_pb2_grpc.add_RoleServiceServicer_to_server(RoleService(), server)
    server.add_insecure_port('localhost:5009')
    server.start()
    print('Server started, listening on 5009')
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()