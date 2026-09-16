def decode(self, encoding='utf-8', errors='strict'):
    original_class = getattr(self, 'original_class')
    return original_class(super(ColorBytes, self).decode(encoding, errors))