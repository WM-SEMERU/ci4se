def get_block_hash(self, height, id=None, endpoint=None):
    return self._call_endpoint(GET_BLOCK_HASH, params=[height], id=id,
        endpoint=endpoint)