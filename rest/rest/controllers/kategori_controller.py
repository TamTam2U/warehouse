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
