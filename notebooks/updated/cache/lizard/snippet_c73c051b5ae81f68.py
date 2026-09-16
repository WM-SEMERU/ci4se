def addPrivateCertificate(self, subjectName, existingCertificate=None):
    if existingCertificate is None:
        assert '@' not in subjectName, "Don't self-sign user certs!"
        mainDN = DistinguishedName(commonName=subjectName)
        mainKey = KeyPair.generate()
        mainCertReq = mainKey.certificateRequest(mainDN)
        mainCertData = mainKey.signCertificateRequest(mainDN, mainCertReq, 
            lambda dn: True, self.genSerial(subjectName))
        mainCert = mainKey.newCertificate(mainCertData)
    else:
        mainCert = existingCertificate
    self.localStore[subjectName] = mainCert