from pyramid.view import view_config, view_defaults
from pyramid.response import Response

from rest.grpc_client.barangmasuk.barangmasuk_client import BarangMasukClient

import grpc


@view_defaults(route_name="masuk", renderer="json")
class BarangMasukController:
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET")
    def get(self):
        try:
            if self.request.params.get("id") is not None:
                id = self.request.params.get("id")
                item = BarangMasukClient().get_barangmasuk(int(id))

                if item == None:
                    return Response(
                        status=404,
                        json_body={"message": "Item not found"},
                    )
                return item
            items = BarangMasukClient()
            result = items.list_barangmasuk()
            return result

        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )

    @view_config(request_method="POST")
    def create(self):
        # item, tanggalMasuk, supplierID, qty
        try:
            if (
                "item" not in self.request.json_body
                or "tanggalMasuk" not in self.request.json_body
                or "supplierID" not in self.request.json_body
                or "qty" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={
                        "message": "Missing item or tanggalMasuk or supplierID or qty"
                    },
                )
            client = BarangMasukClient()
            result = client.create_barangmasuk(
                self.request.json_body["item"],
                self.request.json_body["tanggalMasuk"],
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
            client = BarangMasukClient()
            result = client.delete_barangmasuk(int(id))

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
    def update(self):
        try:
            if (
                "id" not in self.request.json_body
                or "item" not in self.request.json_body
                or "qty" not in self.request.json_body
                or "supplierID" not in self.request.json_body
                or "tanggalMasuk" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={
                        "message": "Missing id or item or qty or supplierID or tanggalMasuk"
                    },
                )
            id = self.request.json_body["id"]
            client = BarangMasukClient()
            result = client.update_barangmasuk(
                int(id),
                self.request.json_body["item"],
                self.request.json_body["tanggalMasuk"],
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
