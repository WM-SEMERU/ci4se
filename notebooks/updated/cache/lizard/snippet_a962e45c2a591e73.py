def get_group_line(self, data):
    idx = -1
    for key in self.groups:
        i = self.get_group_key_line(data, key)
        if i < idx and i != -1 or idx == -1:
            idx = i
    return idx