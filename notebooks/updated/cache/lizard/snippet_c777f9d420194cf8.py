def xadd(self, stream, fields, message_id=b'*', max_len=None, exact_len=False):
    args = []
    if max_len is not None:
        if exact_len:
            args.extend((b'MAXLEN', max_len))
        else:
            args.extend((b'MAXLEN', b'~', max_len))
    args.append(message_id)
    for k, v in fields.items():
        args.extend([k, v])
    return self.execute(b'XADD', stream, *args)