def _link_for_value(self, value):
    try:
        key = Key(value)
        if key.name == self.sentinel:
            return key.parent
    except:
        pass
    return None