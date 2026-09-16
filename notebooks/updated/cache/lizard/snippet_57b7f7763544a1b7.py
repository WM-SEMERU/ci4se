def cleaned_data(self):
    if not hasattr(self, '_cleaned_data'):
        self._cleaned_data = {}
        self.is_valid()
    return self._cleaned_data