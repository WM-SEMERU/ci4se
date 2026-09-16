def fetch_email(M, msg_id):
    res, data = M.fetch(msg_id, '(RFC822)')
    if res == 'OK':
        raw_msg_txt = data[0][1]
        try:
            msg = email.message_from_bytes(raw_msg_txt)
        except AttributeError:
            msg = email.message_from_string(raw_msg_txt)
        return msg
    else:
        return None