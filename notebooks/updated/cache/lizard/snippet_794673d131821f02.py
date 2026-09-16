def AllFieldsFromDescriptor(self, message_descriptor):
    self.Clear()
    for field in message_descriptor.fields:
        self.paths.append(field.name)