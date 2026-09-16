def add_link(self, obj, tag=None):
    if isinstance(obj, tuple):
        newlink = obj
    else:
        newlink = obj.bucket.name, obj.key, tag
    self.links.append(newlink)
    return self._robject