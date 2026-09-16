def to_json(self):
    data = json.dumps(self)
    out = '{"%s":%s}' % (self.schema['title'], data)
    return out