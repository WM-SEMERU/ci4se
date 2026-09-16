def get_attribute(self, code, default=None):
    try:
        return self.get(code=code).value
    except models.ObjectDoesNotExist:
        return default