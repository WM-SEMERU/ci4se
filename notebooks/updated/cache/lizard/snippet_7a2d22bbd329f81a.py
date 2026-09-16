def dump(self, config, instance, file_object, prefer=None, **kwargs):
    file_object.write(self.dumps(config, instance, prefer=prefer, **kwargs))