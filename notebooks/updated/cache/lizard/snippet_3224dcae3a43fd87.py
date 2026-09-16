def clean_up_inverse(self, current):
    if not self.inv_ext:
        return
    index = len(current) - 1
    while index >= 0:
        if isinstance(current[index], InvPlaceholder):
            content = current[index + 1:]
            content.append(_EOP if not self.pathname else self.path_eop)
            current[index] = ''.join(content) + _EXCLA_GROUP_CLOSE % str(
                current[index])
        index -= 1
    self.inv_ext = 0