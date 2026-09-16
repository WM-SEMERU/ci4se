def final(self, style='pkcs7'):
    assert self.mode not in (MODE_XTS, MODE_CMAC)
    if self.ed == b'e':
        if self.mode in (MODE_OFB, MODE_CFB, MODE_CTR):
            dummy = b'0' * (self.chain.totalbytes % self.blocksize)
        else:
            dummy = self.chain.cache
        pdata = pad(dummy, self.blocksize, style=style)[len(dummy):]
        return self.chain.update(pdata, b'e')
    else:
        pass