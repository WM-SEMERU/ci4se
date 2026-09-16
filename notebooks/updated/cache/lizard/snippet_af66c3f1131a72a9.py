def validate(self, answer):
    if answer is None:
        return False
    elif isinstance(self.validator, list):
        for v in self.validator:
            if not v.validate(answer):
                return False
        return True
    else:
        return self.validator.validate(answer)