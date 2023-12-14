# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import barangkeluar_pb2 as barangkeluar__pb2


class BarangKeluarServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.list = channel.unary_unary(
                '/barangkeluar.BarangKeluarService/list',
                request_serializer=barangkeluar__pb2.BarangKeluarListRequest.SerializeToString,
                response_deserializer=barangkeluar__pb2.BarangKeluarListResponse.FromString,
                )
        self.get = channel.unary_unary(
                '/barangkeluar.BarangKeluarService/get',
                request_serializer=barangkeluar__pb2.BarangKeluarDetailRequest.SerializeToString,
                response_deserializer=barangkeluar__pb2.BarangKeluarDetailResponse.FromString,
                )
        self.create = channel.unary_unary(
                '/barangkeluar.BarangKeluarService/create',
                request_serializer=barangkeluar__pb2.BarangKeluarCreateRequest.SerializeToString,
                response_deserializer=barangkeluar__pb2.BarangKeluarCreateResponse.FromString,
                )
        self.update = channel.unary_unary(
                '/barangkeluar.BarangKeluarService/update',
                request_serializer=barangkeluar__pb2.BarangKeluarUpdateRequest.SerializeToString,
                response_deserializer=barangkeluar__pb2.BarangKeluarUpdateResponse.FromString,
                )
        self.delete = channel.unary_unary(
                '/barangkeluar.BarangKeluarService/delete',
                request_serializer=barangkeluar__pb2.BarangKeluarDeleteRequest.SerializeToString,
                response_deserializer=barangkeluar__pb2.BarangKeluarDeleteResponse.FromString,
                )


class BarangKeluarServiceServicer(object):
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


def add_BarangKeluarServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=barangkeluar__pb2.BarangKeluarListRequest.FromString,
                    response_serializer=barangkeluar__pb2.BarangKeluarListResponse.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=barangkeluar__pb2.BarangKeluarDetailRequest.FromString,
                    response_serializer=barangkeluar__pb2.BarangKeluarDetailResponse.SerializeToString,
            ),
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=barangkeluar__pb2.BarangKeluarCreateRequest.FromString,
                    response_serializer=barangkeluar__pb2.BarangKeluarCreateResponse.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=barangkeluar__pb2.BarangKeluarUpdateRequest.FromString,
                    response_serializer=barangkeluar__pb2.BarangKeluarUpdateResponse.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=barangkeluar__pb2.BarangKeluarDeleteRequest.FromString,
                    response_serializer=barangkeluar__pb2.BarangKeluarDeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'barangkeluar.BarangKeluarService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BarangKeluarService(object):
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
        return grpc.experimental.unary_unary(request, target, '/barangkeluar.BarangKeluarService/list',
            barangkeluar__pb2.BarangKeluarListRequest.SerializeToString,
            barangkeluar__pb2.BarangKeluarListResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/barangkeluar.BarangKeluarService/get',
            barangkeluar__pb2.BarangKeluarDetailRequest.SerializeToString,
            barangkeluar__pb2.BarangKeluarDetailResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/barangkeluar.BarangKeluarService/create',
            barangkeluar__pb2.BarangKeluarCreateRequest.SerializeToString,
            barangkeluar__pb2.BarangKeluarCreateResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/barangkeluar.BarangKeluarService/update',
            barangkeluar__pb2.BarangKeluarUpdateRequest.SerializeToString,
            barangkeluar__pb2.BarangKeluarUpdateResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/barangkeluar.BarangKeluarService/delete',
            barangkeluar__pb2.BarangKeluarDeleteRequest.SerializeToString,
            barangkeluar__pb2.BarangKeluarDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
