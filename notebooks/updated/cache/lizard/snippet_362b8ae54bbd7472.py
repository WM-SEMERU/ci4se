def generate_challenge(self):
    from two_factor.utils import totp_digits
    no_digits = totp_digits()
    token = str(totp(self.bin_key, digits=no_digits)).zfill(no_digits)
    if self.method == 'call':
        make_call(device=self, token=token)
    else:
        send_sms(device=self, token=token)