def get(self, idx, default=None):
    for placeholder in self:
        if placeholder.element.ph_idx == idx:
            return placeholder
    return default