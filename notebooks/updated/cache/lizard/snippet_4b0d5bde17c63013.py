def get(self, name=None):
    return self.app.shared_objects.get(name, self.plugin)