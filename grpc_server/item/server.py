from concurrent import futures
import time
import logging
import grpc
import item_pb2
import item_pb2_grpc

import traceback

from database.config import engine
from sqlalchemy import insert, text, values, select, update, delete, desc

from model.item import Item


class ItemService(item_pb2_grpc.ItemServiceServicer):
    def list(self, request, context):
        try:
            with engine.connect() as conn:
                result = conn.execute(select(Item).order_by(desc(Item.id)))
                item = []
                for row in result:
                    item.append(
                        item_pb2.Item(id=row[0], name=row[1], kategoriId=row[2])
                    )
                return item_pb2.ItemListResponse(item=item)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return

    def detail(self, request, context):
        try:
            with engine.connect() as conn:
                response = conn.execute(
                    select(Item).where(Item.id == request.id)
                ).first()
                conn.commit()
                if response is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    return item_pb2.ItemDetailResponse(item=None)
                return item_pb2.ItemDetailResponse(
                    item=item_pb2.Item(
                        id=response[0], name=response[1], kategoriId=response[2]
                    )
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return

    def delete(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(delete(Item).where(Item.id == request.id))
                db.commit()
                if response is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    return item_pb2.ItemDeleteResponse()
                return item_pb2.ItemDeleteResponse(message="Success Deleted")
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
                    insert(Item).values(
                        name=request.name, kategoriId=request.kategoriId
                    )
                )
                db.commit()
                if response is None:
                    context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                    return item_pb2.ItemCreateResponse(item=None)
                return item_pb2.ItemCreateResponse(
                    item=item_pb2.Item(
                        id=response.inserted_primary_key_rows[0][0],
                        name=request.name,
                        kategoriId=request.kategoriId,
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
                    update(Item)
                    .where(Item.id == request.id)
                    .values(name=request.name)
                )
                db.commit()
                if response is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    return item_pb2.ItemUpdateResponse(item=None)
                return item_pb2.ItemUpdateResponse(
                    item=item_pb2.Item(
                        id=request.id, name=request.name,
                    )
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    item_pb2_grpc.add_ItemServiceServicer_to_server(ItemService(), server)
    server.add_insecure_port("localhost:5005")
    server.start()
    print("Server started, listening on 5005")
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()
    