def get_comparable_values(self):
    return str(self.name), str(self.description), str(self.type), bool(self
        .optional), str(self.constraints) if isinstance(self, Constraintable
        ) else ''