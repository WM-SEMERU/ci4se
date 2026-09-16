def check(self, message, ecc, k=None):
    if not k:
        k = self.k
    message, _ = self.pad(message, k=k)
    ecc, _ = self.rpad(ecc, k=k)
    if self.algo == 1 or self.algo == 2:
        return self.ecc_manager.check_fast(message + ecc, k=k)
    elif self.algo == 3 or self.algo == 4:
        return reedsolo.rs_check(bytearray(message + ecc), self.n - k, fcr=
            self.fcr, generator=self.gen_nb)