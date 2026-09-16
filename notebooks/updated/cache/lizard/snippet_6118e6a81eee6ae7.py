def get_lmv2_response(domain, username, password, server_challenge,
    client_challenge):
    ntlmv2_hash = PasswordAuthentication.ntowfv2(domain, username, password
        .encode('utf-16le'))
    hmac_context = hmac.HMAC(ntlmv2_hash, hashes.MD5(), backend=
        default_backend())
    hmac_context.update(server_challenge)
    hmac_context.update(client_challenge)
    lmv2_hash = hmac_context.finalize()
    session_key = hmac.HMAC(ntlmv2_hash, hashes.MD5(), backend=
        default_backend())
    session_key.update(lmv2_hash)
    return lmv2_hash + client_challenge, session_key.finalize()