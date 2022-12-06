
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ..gooseai import generation_pb2 as gooseai_dot_generation__pb2

class GenerationServiceStub(object):
    '\n    gRPC services\n\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.Generate = channel.unary_stream('/gooseai.GenerationService/Generate', request_serializer=gooseai_dot_generation__pb2.Request.SerializeToString, response_deserializer=gooseai_dot_generation__pb2.Answer.FromString)
        self.ChainGenerate = channel.unary_stream('/gooseai.GenerationService/ChainGenerate', request_serializer=gooseai_dot_generation__pb2.ChainRequest.SerializeToString, response_deserializer=gooseai_dot_generation__pb2.Answer.FromString)

class GenerationServiceServicer(object):
    '\n    gRPC services\n\n    '

    def Generate(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChainGenerate(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_GenerationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'Generate': grpc.unary_stream_rpc_method_handler(servicer.Generate, request_deserializer=gooseai_dot_generation__pb2.Request.FromString, response_serializer=gooseai_dot_generation__pb2.Answer.SerializeToString), 'ChainGenerate': grpc.unary_stream_rpc_method_handler(servicer.ChainGenerate, request_deserializer=gooseai_dot_generation__pb2.ChainRequest.FromString, response_serializer=gooseai_dot_generation__pb2.Answer.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('gooseai.GenerationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class GenerationService(object):
    '\n    gRPC services\n\n    '

    @staticmethod
    def Generate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_stream(request, target, '/gooseai.GenerationService/Generate', gooseai_dot_generation__pb2.Request.SerializeToString, gooseai_dot_generation__pb2.Answer.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChainGenerate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_stream(request, target, '/gooseai.GenerationService/ChainGenerate', gooseai_dot_generation__pb2.ChainRequest.SerializeToString, gooseai_dot_generation__pb2.Answer.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
