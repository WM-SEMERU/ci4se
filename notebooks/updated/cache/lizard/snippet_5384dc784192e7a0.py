def clear(self, *args):
    for field in (self.fields_to_clear + list(args)):
        setattr(self, field, None)