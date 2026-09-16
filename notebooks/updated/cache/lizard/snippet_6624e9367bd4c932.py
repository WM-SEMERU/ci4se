def processing_instruction(self, target, data):
    self._element.add_instruction(target, data)
    return self