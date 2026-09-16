def is_identity(self):
    if not self.terms:
        return True
    return len(self.terms) == 1 and not self.terms[0].ops and self.terms[0
        ].coeff == 1.0