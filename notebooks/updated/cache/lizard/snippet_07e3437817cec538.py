def _original_attr(self, attr_name):
    try:
        return getattr(getattr(self.obj.__class__, attr_name),
            '_doubles_target_method', None)
    except AttributeError:
        return None