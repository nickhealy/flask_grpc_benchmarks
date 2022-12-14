# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import grpc_benchmark_pb2 as grpc__benchmark__pb2


class ServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SimpleRequest = channel.unary_unary(
                '/service.Service/SimpleRequest',
                request_serializer=grpc__benchmark__pb2.SimpleRequestInput.SerializeToString,
                response_deserializer=grpc__benchmark__pb2.SimpleRequestOutput.FromString,
                )
        self.ComplexRequest = channel.unary_unary(
                '/service.Service/ComplexRequest',
                request_serializer=grpc__benchmark__pb2.ComplexRequestInput.SerializeToString,
                response_deserializer=grpc__benchmark__pb2.ComplexRequestOutput.FromString,
                )


class ServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SimpleRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ComplexRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SimpleRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.SimpleRequest,
                    request_deserializer=grpc__benchmark__pb2.SimpleRequestInput.FromString,
                    response_serializer=grpc__benchmark__pb2.SimpleRequestOutput.SerializeToString,
            ),
            'ComplexRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.ComplexRequest,
                    request_deserializer=grpc__benchmark__pb2.ComplexRequestInput.FromString,
                    response_serializer=grpc__benchmark__pb2.ComplexRequestOutput.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'service.Service', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Service(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SimpleRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/service.Service/SimpleRequest',
            grpc__benchmark__pb2.SimpleRequestInput.SerializeToString,
            grpc__benchmark__pb2.SimpleRequestOutput.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ComplexRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/service.Service/ComplexRequest',
            grpc__benchmark__pb2.ComplexRequestInput.SerializeToString,
            grpc__benchmark__pb2.ComplexRequestOutput.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
