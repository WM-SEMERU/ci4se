def create_token(self, user):
    h = crypto.pbkdf2(self.get_revocation_key(user), self.salt, self.
        iterations, digest=self.digest)
    return self.sign(self.packer.pack_pk(user.pk) + h)