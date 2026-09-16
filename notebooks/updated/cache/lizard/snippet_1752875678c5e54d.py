def finish_async_rpc(self, address, rpc_id, *response):
    self.verify_calling_thread(True,
        'All asynchronous rpcs must be finished from within the emulation loop'
        )
    if len(response) == 0:
        response_bytes = b''
    elif len(response) == 1:
        response_bytes = response[0]
        if not isinstance(response_bytes, (bytes, bytearray)):
            raise ArgumentError(
                'When passing a binary response to finish_async_rpc, you must pass a bytes or bytearray object'
                , response=response_bytes)
    else:
        resp_format = response[0]
        resp_args = response[1:]
        if not isinstance(resp_format, str):
            raise ArgumentError(
                'When passing a formatted response to finish_async_rpc, you must pass a str object with the format code as the first parameter after the rpc id.'
                , resp_format=resp_format, additional_args=resp_args)
        response_bytes = pack_rpc_payload(resp_format, resp_args)
    self._rpc_queue.finish_async_rpc(address, rpc_id, response_bytes)