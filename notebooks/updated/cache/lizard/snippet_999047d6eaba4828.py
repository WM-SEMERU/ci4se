def get_path(self):
    if self.section:
        return self.section.get_path() + (self.name,)
    else:
        return self.name,