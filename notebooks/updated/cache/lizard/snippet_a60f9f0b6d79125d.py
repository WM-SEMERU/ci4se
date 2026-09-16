def make_otp_response(vres, client_key):
    if client_key is not None:
        sig = make_signature(vres, client_key)
        vres['h'] = sig
    pairs = [(x + '=' + ''.join(vres[x])) for x in sorted(vres.keys())]
    return '\n'.join(pairs)