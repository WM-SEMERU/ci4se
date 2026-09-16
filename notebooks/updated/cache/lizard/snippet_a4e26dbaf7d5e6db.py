def encrypt_template(self, enc_key, mac_key, enc_offset):
    to_encrypt = self.tpl_buff[enc_offset:]
    encrypted = aes_enc(enc_key, PKCS7.pad(to_encrypt))
    to_mac = PKCS7.pad(self.tpl_buff[:enc_offset] + encrypted)
    mac = cbc_mac(mac_key, to_mac)
    return to_mac + mac