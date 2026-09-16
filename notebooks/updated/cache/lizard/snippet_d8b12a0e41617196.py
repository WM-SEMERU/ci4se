def is_entailed_by(self, other):
    other = ListCell.coerce(other)
    if other.size() < self.size():
        return False
    if self.value is None:
        return True
    for i, oval in enumerate(other.value):
        if i == len(self.value):
            break
        if hasattr(self.value[i], 'is_entailed_by') and not self.value[i
            ].is_entailed_by(oval):
            return False
        elif self.value[i] != oval:
            return False
    return True