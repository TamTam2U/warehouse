from concurrent import futures
import time
import logging
import grpc
import kategori_pb2
import kategori_pb2_grpc
import traceback

from database.config import engine
from sqlalchemy import insert, text, values, select, update, delete, desc

from model.kategori import Kategori


class KategoriService(kategori_pb2_grpc.KategoriServiceServicer):
    def list(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(select(Kategori).order_by(desc(Kategori.id)))
                kategori = []
                for row in response:
                    kategori.append(
                        kategori_pb2.Kategori(
                            id=row[0],
                            kategori=row[1],
                        )
                    )
                return kategori_pb2.KategoriListResponse(kategori=kategori)
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
                    select(Kategori).where(Kategori.id == request.id)
                ).first()

                db.commit()

                if res is None:
                    return kategori_pb2.KategoriDetailResponse(kategori=None)
                return kategori_pb2.KategoriDetailResponse(
                    kategori=kategori_pb2.Kategori(
                        id=res[0],
                        kategori=res[1],
                    )
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return None

    def create(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(
                    insert(Kategori).values(kategori=request.kategori)
                )
                db.commit()
                if response is None:
                    return kategori_pb2.KategoriCreateResponse(kategori=None)
                return kategori_pb2.KategoriCreateResponse(
                    kategori=kategori_pb2.Kategori(
                        id=response.inserted_primary_key_rows[0][0],
                        kategori=request.kategori,
                    )
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return None

    def update(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(
                    update(Kategori)
                    .where(Kategori.id == request.id)
                    .values(kategori=request.kategori)
                )
                db.commit()
                if response is None:
                    return kategori_pb2.KategoriUpdateResponse(kategori=None)
                return kategori_pb2.KategoriUpdateResponse(
                    kategori=kategori_pb2.Kategori(
                        id=request.id, kategori=request.kategori
                    )
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return None

    def delete(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(delete(Kategori).where(Kategori.id == request.id))
                db.commit()
                if response is None:
                    return kategori_pb2.KategoriDeleteResponse(message=None)
                return kategori_pb2.KategoriDeleteResponse(message="Berhasili terhapus")
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return None

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    kategori_pb2_grpc.add_KategoriServiceServicer_to_server(
        KategoriService(), server
    )
    server.add_insecure_port("localhost:5007")
    server.start()
    print("Server started, listening on 5007")
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()
