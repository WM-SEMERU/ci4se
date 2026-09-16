def hash(self):
    return ''.join([self.alias, self.description, str(self.ignored), str(
        self.flags)])