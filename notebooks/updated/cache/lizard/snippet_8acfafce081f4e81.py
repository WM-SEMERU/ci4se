def hash_password(self, plain_password):
    salt = uuid.uuid4().hex
    encrypted_password = self.get_hash(salt, plain_password)
    return salt + '$' + encrypted_password