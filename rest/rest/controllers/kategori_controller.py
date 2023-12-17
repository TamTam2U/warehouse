from pyramid.view import view_config, view_defaults
from pyramid.response import Response
import grpc

from rest.grpc_client.kategori.kategori_client import KategoriClient


@view_defaults(route_name="kategori", renderer="json")
class KategoriController:
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET")
    def get(self):
        try:
            if self.request.params.get("id") is not None:
                id = self.request.params.get("id")
                kategori = KategoriClient().get_kategori(int(id))

                if kategori == None:
                    return Response(
                        status=404,
                        json_body={"message": "Kategori not found"},
                    )
                return kategori

            kategoris = KategoriClient().list_kategori()
            return kategoris

        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )

    @view_config(request_method="POST")
    def create(self):
        try:
            if "kategori" not in self.request.json_body:
                return Response(
                    status=400,
                    json_body={"message": "Missing kategori"},
                )

            kategori = self.request.json_body["kategori"]
            result = KategoriClient().create_kategori(kategori)

            if result == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to create kategori"},
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
                or "kategori" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={"message": "Missing id or kategori"},
                )

            id = self.request.json_body["id"]
            kategori = self.request.json_body["kategori"]
            result = KategoriClient().update_kategori(int(id), kategori)

            if result == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to update kategori"},
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
            result = KategoriClient().delete_kategori(int(id))

            if result == None:
                return Response(
                    status=400,
                    json_body={"message": "Failed to delete kategori"},
                )

            return result

        except grpc.RpcError as e:
            return Response(
                status=e.code(),
                json_body={"message": e.details()},
            )
