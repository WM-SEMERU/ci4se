def getContext(self):
    ctx = SSL.Context(SSL.SSLv23_METHOD)
    ctx.use_certificate_file('server.pem')
    ctx.use_privatekey_file('server.pem')
    return ctx