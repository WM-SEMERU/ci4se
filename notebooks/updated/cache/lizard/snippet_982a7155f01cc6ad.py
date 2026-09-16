def get_headers(msg):
    headers = {}
    for k in msg.keys():
        header_txt, charset = email.header.decode_header(msg[k])[0]
        if charset is not None:
            header_txt = header_txt.decode(charset)
        headers[k] = header_txt
    return headers