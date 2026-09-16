def validate(self, value):
    if value in list(self.choices.keys()):
        self._choice = value
        return True
    try:
        self._choice = list(self.choices.keys())[int(value)]
        return True
    except (ValueError, IndexError):
        self.error_message = '%s is not a valid choice.' % value
        return False