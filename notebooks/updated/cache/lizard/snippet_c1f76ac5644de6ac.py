def get_comparable_values_for_ordering(self):
    return 0 if self.position >= 0 else 1, int(self.position), str(self.name
        ), str(self.description)