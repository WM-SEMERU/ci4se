def _call_rpc(self, header):
    length, _, cmd, feature, address = struct.unpack('<BBBBB', bytes(header))
    rpc_id = feature << 8 | cmd
    payload = self.rpc_payload[:length]
    status = 1 << 6
    try:
        response = self.device.call_rpc(address, rpc_id, bytes(payload))
        if len(response) > 0:
            status |= 1 << 7
    except (RPCInvalidIDError, RPCNotFoundError):
        status = 2
        response = b''
    except TileNotFoundError:
        status = 255
        response = b''
    except Exception:
        status = 3
        response = b''
        self._logger.exception(
            'Exception raise while calling rpc, header=%s, payload=%s',
            header, payload)
    self._audit('RPCReceived', rpc_id=rpc_id, address=address, payload=
        binascii.hexlify(payload), status=status, response=binascii.hexlify
        (response))
    resp_header = struct.pack('<BBBB', status, 0, 0, len(response))
    if len(response) > 0:
        self._send_rpc_response((ReceiveHeaderChar.value_handle,
            resp_header), (ReceivePayloadChar.value_handle, response))
    else:
        self._send_rpc_response((ReceiveHeaderChar.value_handle, resp_header))