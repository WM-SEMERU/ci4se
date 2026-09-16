def set_value(self, labels, value):
    if labels:
        self._label_names_correct(labels)
    with mutex:
        self.values[labels] = value