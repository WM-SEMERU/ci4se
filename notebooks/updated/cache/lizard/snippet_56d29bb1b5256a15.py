def dump(self, obj):
    self.references = []
    self.object_obj = obj
    self.object_stream = BytesIO()
    self._writeStreamHeader()
    self.writeObject(obj)
    return self.object_stream.getvalue()