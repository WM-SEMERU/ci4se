def getValidCertifications(self):
    certs = []
    today = date.today()
    for c in self.getCertifications():
        validfrom = c.getValidFrom() if c else None
        validto = c.getValidTo() if validfrom else None
        if not validfrom or not validto:
            continue
        validfrom = validfrom.asdatetime().date()
        validto = validto.asdatetime().date()
        if today >= validfrom and today <= validto:
            certs.append(c)
    return certs