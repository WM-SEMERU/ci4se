def is_full_mxid(user_string):
    if not user_string[0] == '@':
        return False
    parts = user_string[1:].split(':')
    localpart_chars = ascii_lowercase + digits + '._-='
    if not (len(parts) == 2 and all([(i in localpart_chars) for i in parts[0]])
        ):
        return False
    return True