def render_tooltip(self, tooltip, obj):
    if self.tooltip_attr:
        val = getattr(obj, self.tooltip_attr)
    elif self.tooltip_value:
        val = self.tooltip_value
    else:
        return False
    setter = getattr(tooltip, TOOLTIP_SETTERS.get(self.tooltip_type))
    if self.tooltip_type in TOOLTIP_SIZED_TYPES:
        setter(val, self.tooltip_image_size)
    else:
        setter(val)
    return True