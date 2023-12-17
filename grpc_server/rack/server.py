from concurrent import futures
import time
import logging
import grpc
import rack_pb2
import rack_pb2_grpc
import traceback

from database.config import engine
from sqlalchemy import insert, text, values, select, update, delete, desc

from model.rack import Rack


class RackService(rack_pb2_grpc.RackServiceServicer):
    def list(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(select(Rack).order_by(desc(Rack.id)))
                rack = []
                for row in response:
                    rack.append(
                        rack_pb2.Rack(
                            id=row[0],
                            name=row[1],
                        )
                    )
                return rack_pb2.RackListResponse(rack=rack)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return rack_pb2.RackListResponse()

    def get(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(select(Rack).where(Rack.id == request.id)).first()
                db.commit()
                if response is None:
                    return rack_pb2.RackDetailResponse(rack=None)
                return rack_pb2.RackDetailResponse(
                    rack=rack_pb2.Rack(
                        id=response[0],
                        name=response[1],
                    )
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return rack_pb2.RackResponse()

    def create(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(insert(Rack).values(name=request.name))
                db.commit()
                return rack_pb2.RackCreateResponse(
                    rack=rack_pb2.Rack(
                        id=response.inserted_primary_key_rows[0][0], name=request.name
                    )
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return rack_pb2.RackCreateResponse()

    def update(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(
                    update(Rack).where(Rack.id == request.id).values(name=request.name)
                )
                db.commit()
                return rack_pb2.RackUpdateResponse(
                    rack=rack_pb2.Rack(id=request.id, name=request.name)
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return rack_pb2.RackUpdateResponse()

    def delete(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(delete(Rack).where(Rack.id == request.id))
                db.commit()
                return rack_pb2.RackDeleteResponse(message="Rack deleted successfully")
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return rack_pb2.RackDeleteResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rack_pb2_grpc.add_RackServiceServicer_to_server(RackService(), server)
    server.add_insecure_port("localhost:5008")
    server.start()
    print("Server started, listening on 5008")
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()
