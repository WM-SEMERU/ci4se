def parameters(self):
    if self._coord_type == 'galactic':
        return collections.OrderedDict((('l', self.l), ('b', self.b)))
    else:
        return collections.OrderedDict((('ra', self.ra), ('dec', self.dec)))