def h_v_t(header, key):
    if key not in header:
        key = key.title()
        if key not in header:
            raise ValueError('Unexpected header in response, missing: ' +
                key + ' headers:\n' + str(header))
    return header[key]