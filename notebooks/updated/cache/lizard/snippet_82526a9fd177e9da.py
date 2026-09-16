def _tls_auth_decrypt(self, s):
    rcs = self.tls_session.rcs
    read_seq_num = struct.pack('!Q', rcs.seq_num)
    rcs.seq_num += 1
    try:
        return rcs.cipher.auth_decrypt(b'', s, read_seq_num)
    except CipherError as e:
        return e.args
    except AEADTagError as e:
        pkt_info = self.firstlayer().summary()
        log_runtime.info('TLS: record integrity check failed [%s]', pkt_info)
        return e.args