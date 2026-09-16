def validate(self, sig=None):
    if sig is not None:
        sig_mtime, sig_size, sig_md5 = sig
    else:
        try:
            with open(self.sig_file()) as sig:
                sig_mtime, sig_size, sig_md5 = sig.read().strip().split()
        except:
            return False
    if not self.exists():
        if (self + '.zapped').is_file():
            with open(self + '.zapped') as sig:
                line = sig.readline()
                return sig_md5 == line.strip().rsplit('\t', 3)[-1]
        else:
            return False
    if sig_mtime == os.path.getmtime(self) and sig_size == os.path.getsize(self
        ):
        return True
    return fileMD5(self) == sig_md5