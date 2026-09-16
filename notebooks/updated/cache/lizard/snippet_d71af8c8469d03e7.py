def sql(self):
    assert self.in_key and not self.nullable
    return '`{name}` {type} NOT NULL COMMENT "{comment}"'.format(name=self.
        name, type=self.type, comment=self.comment)