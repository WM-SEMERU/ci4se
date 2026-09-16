def formatted_description(self):
    desc = self.description
    if desc:
        return desc.replace('%s1', self.formatted_value)
    else:
        return None