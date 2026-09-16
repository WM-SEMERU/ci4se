def link_in(self, other, preserve=False):
    if preserve:
        other = other.clone()
    link_modules(self, other)