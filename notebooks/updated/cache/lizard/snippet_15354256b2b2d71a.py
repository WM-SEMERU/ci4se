def hash(self):
    hashed = super(ForEach, self).hash()
    return khash(hashed + self._mutated_field.hash())