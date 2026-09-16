def xml(self):
    root = Element('UsernameToken', ns=wssens)
    u = Element('Username', ns=wssens)
    u.setText(self.username)
    root.append(u)
    p = Element('Password', ns=wssens)
    p.setText(self.password)
    if self.password_digest:
        p.set('Type', wsdigest)
        p.setText(self.password_digest)
    root.append(p)
    if self.nonce is not None:
        n = Element('Nonce', ns=wssens)
        if self.nonce_has_encoding:
            n.set('EncodingType', nonce_encoding_type)
        n.setText(self.nonce)
        root.append(n)
    if self.created is not None:
        n = Element('Created', ns=wsuns)
        n.setText(str(DateTime(self.created)))
        root.append(n)
    return root