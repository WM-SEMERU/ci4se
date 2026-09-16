def set_default(self_, param_name, value):
    cls = self_.cls
    setattr(cls, param_name, value)