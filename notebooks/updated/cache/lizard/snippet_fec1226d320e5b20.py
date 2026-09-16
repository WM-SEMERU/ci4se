def decrypt(self, orig_pkt, assoclen=None):
    hdr = copy.deepcopy(orig_pkt)
    del hdr[MACsec].payload
    pktlen = len(orig_pkt)
    if self.send_sci:
        hdrlen = NOSCI_LEN + SCI_LEN
    else:
        hdrlen = NOSCI_LEN
    if assoclen is None or not self.do_encrypt:
        if self.do_encrypt:
            assoclen = hdrlen
        else:
            assoclen = pktlen - self.icvlen
    iv = self.make_iv(hdr)
    assoc, ct, icv = MACsecSA.split_pkt(orig_pkt, assoclen, self.icvlen)
    decryptor = Cipher(algorithms.AES(self.key), modes.GCM(iv, icv),
        backend=default_backend()).decryptor()
    decryptor.authenticate_additional_data(assoc)
    pt = assoc[hdrlen:assoclen]
    pt += decryptor.update(ct)
    pt += decryptor.finalize()
    hdr[MACsec].type = struct.unpack('!H', pt[0:2])[0]
    hdr[MACsec].payload = Raw(pt[2:])
    return hdr