def build(self, builder):
    builder.start('CheckValue', {})
    builder.data(str(self.value))
    builder.end('CheckValue')