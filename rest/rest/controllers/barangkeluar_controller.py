from pyramid.view import view_config, view_defaults
from pyramid.response import Response

from rest.grpc_client.barangkeluar.barangkeluar_client import BarangKeluarClient

import grpc


@view_defaults(route_name="keluar", renderer="json")
class BarangKeluarController:
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET")
    def get(self):
        try:
            if self.request.params.get("id") is not None:
                id = self.request.params.get("id")
                item = BarangKeluarClient().get_barangkeluar(int(id))

                if item == None:
                    return Response(
                        status=404,
                        json_body={"message": "Item not found"},
                    )
                return item
            items = BarangKeluarClient().list_barangkeluar()
            return items

        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )

    @view_config(request_method="POST")
    def post(self):
        try:
            if (
                "item" not in self.request.json_body
                or "tanggalKeluar" not in self.request.json_body
                or "supplierID" not in self.request.json_body
                or "qty" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={
                        "message": "Missing item or tanggalKeluar or supplierID or qty"
                    },
                )

            client = BarangKeluarClient()
            result = client.create_barangkeluar(
                self.request.json_body["item"],
                self.request.json_body["tanggalKeluar"],
                self.request.json_body["supplierID"],
                int(self.request.json_body["qty"]),
            )

            if result == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to create item"},
                )
            return result

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
            client = BarangKeluarClient()
            result = client.delete_barangkeluar(int(id))

            if result == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to delete item"},
                )
            return result
        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )

    @view_config(request_method="PUT")
    def put(self):
        try:
            if (
                "id" not in self.request.json_body
                or "item" not in self.request.json_body
                or "tanggalKeluar" not in self.request.json_body
                or "supplierID" not in self.request.json_body
                or "qty" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={
                        "message": "Missing id or item or tanggalKeluar or supplierID or qty"
                    },
                )

            client = BarangKeluarClient()
            result = client.update_barangkeluar(
                self.request.json_body["id"],
                self.request.json_body["item"],
                self.request.json_body["tanggalKeluar"],
                self.request.json_body["supplierID"],
                int(self.request.json_body["qty"]),
            )

            if result == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to update item"},
                )
            return result

        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )
