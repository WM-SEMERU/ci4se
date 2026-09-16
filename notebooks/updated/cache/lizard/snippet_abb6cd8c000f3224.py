def calc_resp(password_hash, server_challenge):
    password_hash += b'\x00' * (21 - len(password_hash))
    res = b''
    dobj = des.DES(password_hash[0:7])
    res = res + dobj.encrypt(server_challenge[0:8])
    dobj = des.DES(password_hash[7:14])
    res = res + dobj.encrypt(server_challenge[0:8])
    dobj = des.DES(password_hash[14:21])
    res = res + dobj.encrypt(server_challenge[0:8])
    return res