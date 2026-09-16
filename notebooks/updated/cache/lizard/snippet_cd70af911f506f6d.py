def get_block(self, x, y, z):
    sy, by = divmod(y, 16)
    section = self.get_section(sy)
    if section == None:
        return None
    return section.get_block(x, by, z)