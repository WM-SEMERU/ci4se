def save(self):
    data = super().save()
    data['expr'] = self.expr.pattern
    data['default_end'] = self.default_end
    return data