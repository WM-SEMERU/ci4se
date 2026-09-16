def body_line_iterator(msg, decode=False):
    for subpart in msg.walk():
        payload = subpart.get_payload(decode=decode)
        if isinstance(payload, str):
            for line in StringIO(payload):
                yield line