def parse(self, node):
    pm = getattr(self, 'parse_%s' % node.__class__.__name__)
    pm(node)