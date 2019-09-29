# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from libs import rpc_pb2 as rpc__pb2


class ToolsStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.DecodeExtrinsic = channel.unary_unary(
        '/codec_protos.Tools/DecodeExtrinsic',
        request_serializer=rpc__pb2.ExtrinsicRequest.SerializeToString,
        response_deserializer=rpc__pb2.ExtrinsicReply.FromString,
        )
    self.DecodeEvent = channel.unary_unary(
        '/codec_protos.Tools/DecodeEvent',
        request_serializer=rpc__pb2.EventRequest.SerializeToString,
        response_deserializer=rpc__pb2.EventReply.FromString,
        )
    self.DecodeLog = channel.unary_unary(
        '/codec_protos.Tools/DecodeLog',
        request_serializer=rpc__pb2.LogRequest.SerializeToString,
        response_deserializer=rpc__pb2.LogReply.FromString,
        )
    self.DecodeStorage = channel.unary_unary(
        '/codec_protos.Tools/DecodeStorage',
        request_serializer=rpc__pb2.StorageRequest.SerializeToString,
        response_deserializer=rpc__pb2.StorageReply.FromString,
        )


class ToolsServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def DecodeExtrinsic(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DecodeEvent(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DecodeLog(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DecodeStorage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ToolsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'DecodeExtrinsic': grpc.unary_unary_rpc_method_handler(
          servicer.DecodeExtrinsic,
          request_deserializer=rpc__pb2.ExtrinsicRequest.FromString,
          response_serializer=rpc__pb2.ExtrinsicReply.SerializeToString,
      ),
      'DecodeEvent': grpc.unary_unary_rpc_method_handler(
          servicer.DecodeEvent,
          request_deserializer=rpc__pb2.EventRequest.FromString,
          response_serializer=rpc__pb2.EventReply.SerializeToString,
      ),
      'DecodeLog': grpc.unary_unary_rpc_method_handler(
          servicer.DecodeLog,
          request_deserializer=rpc__pb2.LogRequest.FromString,
          response_serializer=rpc__pb2.LogReply.SerializeToString,
      ),
      'DecodeStorage': grpc.unary_unary_rpc_method_handler(
          servicer.DecodeStorage,
          request_deserializer=rpc__pb2.StorageRequest.FromString,
          response_serializer=rpc__pb2.StorageReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'codec_protos.Tools', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
