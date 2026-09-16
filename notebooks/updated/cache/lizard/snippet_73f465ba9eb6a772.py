def _refresh_grpc(operations_stub, operation_name):
    request_pb = operations_pb2.GetOperationRequest(name=operation_name)
    return operations_stub.GetOperation(request_pb)