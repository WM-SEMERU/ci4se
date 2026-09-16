def aes_ecb_encrypt(self, key_handle, plaintext):
    return pyhsm.aes_ecb_cmd.YHSM_Cmd_AES_ECB_Encrypt(self.stick,
        key_handle, plaintext).execute()