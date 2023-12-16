from concurrent import futures
import time
import logging
import grpc
import barangkeluar_pb2
import barangkeluar_pb2_grpc

import traceback

from database.config import engine
from sqlalchemy import insert, text, values, select, update, delete, desc

from model.barangkeluar import BarangKeluar


class BarangKeluarService(barangkeluar_pb2_grpc.BarangKeluarServiceServicer):
    def list(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(
                    select(BarangKeluar).order_by(desc(BarangKeluar.id))
                )
                barangkeluar = []
                for row in response:
                    barangkeluar.append(
                        barangkeluar_pb2.BarangKeluar(
                            id=row[0],
                            item=row[1],
                            tanggalKeluar=row[2],
                            supplierID=row[3],
                            qty=row[4],
                        )
                    )
                return barangkeluar_pb2.BarangKeluarListResponse(
                    barangkeluar=barangkeluar
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return barangkeluar_pb2.BarangKeluarListResponse()

    def get(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(
                    select(BarangKeluar).where(BarangKeluar.id == request.id)
                ).first()

                db.commit()

                if response is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    return barangkeluar_pb2.BarangKeluarDetailResponse(
                        barangkeluar=None
                    )
                return barangkeluar_pb2.BarangKeluarDetailResponse(
                    barangkeluar=barangkeluar_pb2.BarangKeluar(
                        id=response[0],
                        item=response[1],
                        tanggalKeluar=response[2],
                        supplierID=response[3],
                        qty=response[4],
                    )
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return barangkeluar_pb2.BarangKeluarDetailResponse()

    def create(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(
                    insert(BarangKeluar).values(
                        item=request.item,
                        tanggalKeluar=request.tanggalKeluar,
                        supplierID=request.supplierID,
                        qty=request.qty,
                    )
                )

                db.commit()
                return barangkeluar_pb2.BarangKeluarCreateResponse(
                    barangkeluar=barangkeluar_pb2.BarangKeluar(
                        id=response.inserted_primary_key_rows[0][0],
                        item=request.item,
                        tanggalKeluar=request.tanggalKeluar,
                        supplierID=request.supplierID,
                        qty=request.qty,
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
                    update(BarangKeluar)
                    .where(BarangKeluar.id == request.id)
                    .values(
                        item=request.item,
                        tanggalKeluar=request.tanggalKeluar,
                        supplierID=request.supplierID,
                        qty=request.qty,
                    )
                )

                db.commit()
                return barangkeluar_pb2.BarangKeluarUpdateResponse(barangkeluar=
                    barangkeluar_pb2.BarangKeluar(
                        id=request.id,
                        item=request.item,
                        tanggalKeluar=request.tanggalKeluar,
                        supplierID=request.supplierID,
                        qty=request.qty,
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
                response = db.execute(
                    delete(BarangKeluar).where(BarangKeluar.id == request.id)
                )
                db.commit()

                if response is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    return barangkeluar_pb2.BarangKeluarDeleteResponse()

                return barangkeluar_pb2.BarangKeluarDeleteResponse(
                    message="Success Deleted",
                )

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return barangkeluar_pb2.BarangKeluarDeleteResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    barangkeluar_pb2_grpc.add_BarangKeluarServiceServicer_to_server(
        BarangKeluarService(), server
    )
    server.add_insecure_port("localhost:5003")
    server.start()
    print("Server started, listening on 5003")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
