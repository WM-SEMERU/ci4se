def get_storage(self, contract_hash, storage_key, id=None, endpoint=None):
    result = self._call_endpoint(GET_STORAGE, params=[contract_hash,
        binascii.hexlify(storage_key.encode('utf-8')).decode('utf-8')], id=
        id, endpoint=endpoint)
    try:
        return bytearray(binascii.unhexlify(result.encode('utf-8')))
    except Exception as e:
        raise NEORPCException('could not decode result %s ' % e)