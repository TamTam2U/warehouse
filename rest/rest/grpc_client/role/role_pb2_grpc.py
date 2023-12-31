# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import rest.grpc_client.role.role_pb2 as role__pb2


class RoleServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.list = channel.unary_unary(
                '/role.RoleService/list',
                request_serializer=role__pb2.RoleListRequest.SerializeToString,
                response_deserializer=role__pb2.RoleListResponse.FromString,
                )
        self.get = channel.unary_unary(
                '/role.RoleService/get',
                request_serializer=role__pb2.RoleDetailRequest.SerializeToString,
                response_deserializer=role__pb2.RoleDetailResponse.FromString,
                )
        self.create = channel.unary_unary(
                '/role.RoleService/create',
                request_serializer=role__pb2.RoleCreateRequest.SerializeToString,
                response_deserializer=role__pb2.RoleCreateResponse.FromString,
                )
        self.update = channel.unary_unary(
                '/role.RoleService/update',
                request_serializer=role__pb2.RoleUpdateRequest.SerializeToString,
                response_deserializer=role__pb2.RoleUpdateResponse.FromString,
                )
        self.delete = channel.unary_unary(
                '/role.RoleService/delete',
                request_serializer=role__pb2.RoleDeleteRequest.SerializeToString,
                response_deserializer=role__pb2.RoleDeleteResponse.FromString,
                )


class RoleServiceServicer(object):
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


def add_RoleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=role__pb2.RoleListRequest.FromString,
                    response_serializer=role__pb2.RoleListResponse.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=role__pb2.RoleDetailRequest.FromString,
                    response_serializer=role__pb2.RoleDetailResponse.SerializeToString,
            ),
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=role__pb2.RoleCreateRequest.FromString,
                    response_serializer=role__pb2.RoleCreateResponse.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=role__pb2.RoleUpdateRequest.FromString,
                    response_serializer=role__pb2.RoleUpdateResponse.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=role__pb2.RoleDeleteRequest.FromString,
                    response_serializer=role__pb2.RoleDeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'role.RoleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RoleService(object):
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
        return grpc.experimental.unary_unary(request, target, '/role.RoleService/list',
            role__pb2.RoleListRequest.SerializeToString,
            role__pb2.RoleListResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/role.RoleService/get',
            role__pb2.RoleDetailRequest.SerializeToString,
            role__pb2.RoleDetailResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/role.RoleService/create',
            role__pb2.RoleCreateRequest.SerializeToString,
            role__pb2.RoleCreateResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/role.RoleService/update',
            role__pb2.RoleUpdateRequest.SerializeToString,
            role__pb2.RoleUpdateResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/role.RoleService/delete',
            role__pb2.RoleDeleteRequest.SerializeToString,
            role__pb2.RoleDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
