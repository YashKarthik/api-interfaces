
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ..gooseai import engines_pb2 as gooseai_dot_engines__pb2

class EnginesServiceStub(object):
    'Missing associated documentation comment in .proto file.'

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.ListEngines = channel.unary_unary('/gooseai.EnginesService/ListEngines', request_serializer=gooseai_dot_engines__pb2.ListEnginesRequest.SerializeToString, response_deserializer=gooseai_dot_engines__pb2.Engines.FromString)

class EnginesServiceServicer(object):
    'Missing associated documentation comment in .proto file.'

    def ListEngines(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_EnginesServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'ListEngines': grpc.unary_unary_rpc_method_handler(servicer.ListEngines, request_deserializer=gooseai_dot_engines__pb2.ListEnginesRequest.FromString, response_serializer=gooseai_dot_engines__pb2.Engines.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('gooseai.EnginesService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class EnginesService(object):
    'Missing associated documentation comment in .proto file.'

    @staticmethod
    def ListEngines(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gooseai.EnginesService/ListEngines', gooseai_dot_engines__pb2.ListEnginesRequest.SerializeToString, gooseai_dot_engines__pb2.Engines.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
