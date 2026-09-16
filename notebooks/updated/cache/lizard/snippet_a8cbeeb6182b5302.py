def set_bucket_props(self, bucket, props):
    if not self.pb_all_bucket_props():
        for key in props:
            if key not in ('n_val', 'allow_mult'):
                raise NotImplementedError(
                    'Server only supports n_val and allow_mult properties over PBC'
                    )
    msg_code = riak.pb.messages.MSG_CODE_SET_BUCKET_REQ
    codec = self._get_codec(msg_code)
    msg = codec.encode_set_bucket_props(bucket, props)
    resp_code, resp = self._request(msg, codec)
    return True