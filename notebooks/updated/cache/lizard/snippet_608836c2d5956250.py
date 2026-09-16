def signTBSCert(self, tbsCert, h='sha256'):
    sigAlg = tbsCert.signature
    h = h or hash_by_oid[sigAlg.algorithm.val]
    sigVal = self.sign(raw(tbsCert), h=h, t='pkcs')
    c = X509_Cert()
    c.tbsCertificate = tbsCert
    c.signatureAlgorithm = sigAlg
    c.signatureValue = _Raw_ASN1_BIT_STRING(sigVal, readable=True)
    return c