def validate_aead_otp(self, public_id, otp, key_handle, aead):
    if type(public_id) is not str:
        assert ()
    if type(otp) is not str:
        assert ()
    if type(key_handle) is not int:
        assert ()
    if type(aead) is not str:
        assert ()
    return pyhsm.validate_cmd.YHSM_Cmd_AEAD_Validate_OTP(self.stick,
        public_id, otp, key_handle, aead).execute()