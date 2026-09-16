def get_bytes(self):
    ret = struct.pack('<I16s16sQ', client_DH_inner_data.constructor, self.
        nonce, self.server_nonce, self.retry_id)
    bytes_io = BytesIO()
    bytes_io.write(ret)
    serialize_string(bytes_io, self.g_b)
    return bytes_io.getvalue()