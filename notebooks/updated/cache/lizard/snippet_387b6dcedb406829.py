def formfield(self, **kwargs):
    defaults = {'form_class': LocalizedTextFieldForm}
    defaults.update(kwargs)
    return super().formfield(**defaults)