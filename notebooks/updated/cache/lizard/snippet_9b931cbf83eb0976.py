def build(self, builder):
    builder.start('SignatureRef', dict(SignatureOID=self.oid))
    builder.end('SignatureRef')