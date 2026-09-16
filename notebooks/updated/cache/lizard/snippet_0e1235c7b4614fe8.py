async def await_rpc(self, address, rpc_id, *args, **kwargs):
    self.verify_calling_thread(True,
        'await_rpc must be called from **inside** the event loop')
    if isinstance(rpc_id, RPCDeclaration):
        arg_format = rpc_id.arg_format
        resp_format = rpc_id.resp_format
        rpc_id = rpc_id.rpc_id
    else:
        arg_format = kwargs.get('arg_format', None)
        resp_format = kwargs.get('resp_format', None)
    arg_payload = b''
    if arg_format is not None:
        arg_payload = pack_rpc_payload(arg_format, args)
    self._logger.debug('Sending rpc to %d:%04X, payload=%s', address,
        rpc_id, args)
    response = AwaitableResponse()
    self._rpc_queue.put_rpc(address, rpc_id, arg_payload, response)
    try:
        resp_payload = await response.wait(1.0)
    except RPCRuntimeError as err:
        resp_payload = err.binary_error
    if resp_format is None:
        return []
    resp = unpack_rpc_payload(resp_format, resp_payload)
    return resp