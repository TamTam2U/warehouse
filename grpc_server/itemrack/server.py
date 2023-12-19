from concurrent import futures
import time
import logging
import grpc
import itemrack_pb2
import itemrack_pb2_grpc
import traceback

from database.config import engine
from sqlalchemy import insert, text, values, select, update, delete, desc

from model.itemrack import ItemRack


class ItemRackService(itemrack_pb2_grpc.ItemRackServiceServicer):
    def list(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                res = db.execute(select(ItemRack).order_by(desc(ItemRack.id)))
                db.commit()
                itemrack = []
                for row in res:
                    itemrack.append(
                        itemrack_pb2.ItemRack(id=row[0], itemId=row[1], rackId=row[2])
                    )
                return itemrack_pb2.ItemRackListResponse(itemRack=itemrack)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return

    def delete(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                res = db.execute(delete(ItemRack).where(ItemRack.id == request.id))
                db.commit()
                if res is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    return
                return itemrack_pb2.ItemRackDeleteResponse(message="Success Deleted")
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return

    def get(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                res = db.execute(
                    select(ItemRack).where(ItemRack.id == request.id)
                ).first()
                db.commit()
                if res is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    return
                return itemrack_pb2.ItemRackDetailResponse(
                    itemRack=itemrack_pb2.ItemRack(
                        id=res[0], itemId=res[1], rackId=res[2]
                    )
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return

    def create(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(
                    insert(ItemRack).values(
                        itemId=request.itemId, rackId=request.rackId
                    )
                )
                db.commit()
                if response is None:
                    context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                    return
                return itemrack_pb2.ItemRackCreateResponse(
                    itemRack=itemrack_pb2.ItemRack(
                        id=response.inserted_primary_key_rows[0][0],
                        itemId=request.itemId,
                        rackId=request.rackId,
                    )
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return

    def update(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(
                    update(ItemRack)
                    .where(ItemRack.id == request.id)
                    .values(itemId=request.itemId, rackId=request.rackId)
                )
                db.commit()
                if response is None:
                    context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                    return
                return itemrack_pb2.ItemRackUpdateResponse(
                    itemRack=itemrack_pb2.ItemRack(
                        id=request.id, itemId=request.itemId, rackId=request.rackId
                    )
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return

    def itemByRackId(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                res = db.execute(
                    select(ItemRack).where(ItemRack.rackId == request.rackId)
                )
                db.commit()
                itemrack = []
                for row in res:
                    itemrack.append(
                        itemrack_pb2.ItemRack(id=row[0], itemId=row[1], rackId=row[2])
                    )
                return itemrack_pb2.ItemByRackIdResponse(itemRack=itemrack)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    itemrack_pb2_grpc.add_ItemRackServiceServicer_to_server(ItemRackService(), server)
    server.add_insecure_port("localhost:5006")
    server.start()
    print("Server started, listening on 5006")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
