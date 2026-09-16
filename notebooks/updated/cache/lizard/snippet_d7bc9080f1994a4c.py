def save(self):
    id = self.id or self.objects.id(self.name)
    self.objects[id] = self.prepare_save(dict(self))
    self.id = id
    self.post_save()
    return id