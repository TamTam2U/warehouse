from concurrent import futures
import time
import logging
import grpc
import barangmasuk_pb2
import barangmasuk_pb2_grpc

import traceback

from database.config import engine
from sqlalchemy import insert, text, values, select, update, delete, desc

from model.barangmasuk import BarangMasuk


class BarangMasukService(barangmasuk_pb2_grpc.BarangMasukServiceServicer):
    def list(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(
                    select(BarangMasuk).order_by(desc(BarangMasuk.id))
                )
                barangmasuk = []
                for row in response:
                    barangmasuk.append(
                        barangmasuk_pb2.BarangMasuk(
                            id=row[0],
                            item=row[1],
                            tanggalMasuk=row[2],
                            supplierID=row[3],
                            qty=row[4],
                        )
                    )
                return barangmasuk_pb2.BarangMasukListResponse(barangmasuk=barangmasuk)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return

    def get(self, request, context):
        try:
            with engine.connect() as db:
                db.begin()
                response = db.execute(
                    select(BarangMasuk).where(BarangMasuk.id == request.id)
                ).first()
                db.commit()
                if response is None:
                    return barangmasuk_pb2.BarangMasukDetailResponse(barangmasuk=None)
                return barangmasuk_pb2.BarangMasukDetailResponse(
                    barangmasuk=barangmasuk_pb2.BarangMasuk(
                        id=response[0],
                        item=response[1],
                        tanggalMasuk=response[2],
                        supplierID=response[3],
                        qty=response[4],
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
                    insert(BarangMasuk).values(
                        item=request.item,
                        tanggalMasuk=request.tanggalMasuk,
                        supplierID=request.supplierID,
                        qty=request.qty,
                    )
                )
                db.commit()
                if response is None:
                    return barangmasuk_pb2.BarangMasukCreateResponse(barangmasuk=None)
                return barangmasuk_pb2.BarangMasukCreateResponse(
                    barangmasuk=barangmasuk_pb2.BarangMasuk(
                        id=response.inserted_primary_key_rows[0][0],
                        item=request.item,
                        tanggalMasuk=request.tanggalMasuk,
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
                    update(BarangMasuk)
                    .where(BarangMasuk.id == request.id)
                    .values(
                        item=request.item,
                        tanggalMasuk=request.tanggalMasuk,
                        supplierID=request.supplierID,
                        qty=request.qty,
                    )
                )
                db.commit()
                return barangmasuk_pb2.BarangMasukUpdateResponse(
                    barangmasuk=barangmasuk_pb2.BarangMasuk(
                        id=request.id,
                        item=request.item,
                        tanggalMasuk=request.tanggalMasuk,
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
                    delete(BarangMasuk).where(BarangMasuk.id == request.id)
                )
                db.commit()
                if response is None:
                    return barangmasuk_pb2.BarangMasukDeleteResponse(barangmasuk=None)
                return barangmasuk_pb2.BarangMasukDeleteResponse(
                    message="Success Deleted",
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return None

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    barangmasuk_pb2_grpc.add_BarangMasukServiceServicer_to_server(
        BarangMasukService(), server
    )
    server.add_insecure_port("localhost:5004")
    server.start()
    print("Server started, listening on 5004")
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()
