def _setPrivate(self, private):
    self.private = private
    self.public = pow(self.generator, self.private, self.modulus)