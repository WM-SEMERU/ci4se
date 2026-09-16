def _encode_item(self, item):
    if self.encoding.__name__ == 'pickle':
        return self.encoding.dumps(item, protocol=-1)
    else:
        return self.encoding.dumps(item)