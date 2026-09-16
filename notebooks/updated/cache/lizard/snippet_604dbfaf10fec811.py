def decode_contents(self, contents, obj):
    obj.siblings = [self.decode_content(c, RiakContent(obj)) for c in contents]
    if len(obj.siblings) > 1 and obj.resolver is not None:
        obj.resolver(obj)
    return obj