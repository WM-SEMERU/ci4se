def verifymessage(self, address, signature, message):
    return self.req('verifymessage', [address, signature, message])