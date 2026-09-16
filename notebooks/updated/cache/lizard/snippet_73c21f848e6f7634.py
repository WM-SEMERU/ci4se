def get_value(self, consumer=None):
    if consumer:
        self.consumers[consumer] = True
    return self.value