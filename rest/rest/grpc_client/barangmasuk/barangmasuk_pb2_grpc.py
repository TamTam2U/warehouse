# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import rest.grpc_client.barangmasuk.barangmasuk_pb2 as barangmasuk__pb2


class BarangMasukServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.list = channel.unary_unary(
                '/barangmasuk.BarangMasukService/list',
                request_serializer=barangmasuk__pb2.BarangMasukListRequest.SerializeToString,
                response_deserializer=barangmasuk__pb2.BarangMasukListResponse.FromString,
                )
        self.get = channel.unary_unary(
                '/barangmasuk.BarangMasukService/get',
                request_serializer=barangmasuk__pb2.BarangMasukDetailRequest.SerializeToString,
                response_deserializer=barangmasuk__pb2.BarangMasukDetailResponse.FromString,
                )
        self.create = channel.unary_unary(
                '/barangmasuk.BarangMasukService/create',
                request_serializer=barangmasuk__pb2.BarangMasukCreateRequest.SerializeToString,
                response_deserializer=barangmasuk__pb2.BarangMasukCreateResponse.FromString,
                )
        self.update = channel.unary_unary(
                '/barangmasuk.BarangMasukService/update',
                request_serializer=barangmasuk__pb2.BarangMasukUpdateRequest.SerializeToString,
                response_deserializer=barangmasuk__pb2.BarangMasukUpdateResponse.FromString,
                )
        self.delete = channel.unary_unary(
                '/barangmasuk.BarangMasukService/delete',
                request_serializer=barangmasuk__pb2.BarangMasukDeleteRequest.SerializeToString,
                response_deserializer=barangmasuk__pb2.BarangMasukDeleteResponse.FromString,
                )


class BarangMasukServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def list(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BarangMasukServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=barangmasuk__pb2.BarangMasukListRequest.FromString,
                    response_serializer=barangmasuk__pb2.BarangMasukListResponse.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=barangmasuk__pb2.BarangMasukDetailRequest.FromString,
                    response_serializer=barangmasuk__pb2.BarangMasukDetailResponse.SerializeToString,
            ),
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=barangmasuk__pb2.BarangMasukCreateRequest.FromString,
                    response_serializer=barangmasuk__pb2.BarangMasukCreateResponse.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=barangmasuk__pb2.BarangMasukUpdateRequest.FromString,
                    response_serializer=barangmasuk__pb2.BarangMasukUpdateResponse.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=barangmasuk__pb2.BarangMasukDeleteRequest.FromString,
                    response_serializer=barangmasuk__pb2.BarangMasukDeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'barangmasuk.BarangMasukService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BarangMasukService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def list(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/barangmasuk.BarangMasukService/list',
            barangmasuk__pb2.BarangMasukListRequest.SerializeToString,
            barangmasuk__pb2.BarangMasukListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/barangmasuk.BarangMasukService/get',
            barangmasuk__pb2.BarangMasukDetailRequest.SerializeToString,
            barangmasuk__pb2.BarangMasukDetailResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/barangmasuk.BarangMasukService/create',
            barangmasuk__pb2.BarangMasukCreateRequest.SerializeToString,
            barangmasuk__pb2.BarangMasukCreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/barangmasuk.BarangMasukService/update',
            barangmasuk__pb2.BarangMasukUpdateRequest.SerializeToString,
            barangmasuk__pb2.BarangMasukUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/barangmasuk.BarangMasukService/delete',
            barangmasuk__pb2.BarangMasukDeleteRequest.SerializeToString,
            barangmasuk__pb2.BarangMasukDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
