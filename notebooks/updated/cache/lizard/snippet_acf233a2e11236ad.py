def _options_protobuf(self, retry_id):
    if retry_id is not None:
        if self._read_only:
            raise ValueError(_CANT_RETRY_READ_ONLY)
        return types.TransactionOptions(read_write=types.TransactionOptions
            .ReadWrite(retry_transaction=retry_id))
    elif self._read_only:
        return types.TransactionOptions(read_only=types.TransactionOptions.
            ReadOnly())
    else:
        return None