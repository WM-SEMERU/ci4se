def _choice_format(self, occur):
    middle = '%s' if self.rng_children() else '<empty/>%s'
    fmt = self.start_tag() + middle + self.end_tag()
    if self.occur != 2:
        return '<optional>' + fmt + '</optional>'
    else:
        return fmt