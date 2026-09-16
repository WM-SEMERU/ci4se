def get_ntlm2_response(password, server_challenge, client_challenge):
    md5 = hashlib.new('md5')
    md5.update(server_challenge + client_challenge)
    ntlm2_session_hash = md5.digest()[:8]
    ntlm_hash = PasswordAuthentication.ntowfv1(password.encode('utf-16le'))
    response = PasswordAuthentication._encrypt_des_block(ntlm_hash[:7],
        ntlm2_session_hash)
    response += PasswordAuthentication._encrypt_des_block(ntlm_hash[7:14],
        ntlm2_session_hash)
    response += PasswordAuthentication._encrypt_des_block(ntlm_hash[14:],
        ntlm2_session_hash)
    session_hash = hashlib.new('md4')
    session_hash.update(ntlm_hash)
    hmac_context = hmac.HMAC(session_hash.digest(), hashes.MD5(), backend=
        default_backend())
    hmac_context.update(server_challenge + client_challenge)
    return response, hmac_context.finalize()