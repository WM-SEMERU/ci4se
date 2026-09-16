def add_layout(self, obj, place='center'):
    valid_places = ['left', 'right', 'above', 'below', 'center']
    if place not in valid_places:
        raise ValueError(
            "Invalid place '%s' specified. Valid place values are: %s" % (
            place, nice_join(valid_places)))
    getattr(self, place).append(obj)