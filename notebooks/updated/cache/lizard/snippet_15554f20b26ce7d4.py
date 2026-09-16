def andor_tags(self):
    if not self.is_andor:
        return None
    tags = self.tags
    result = {'Id': tags['AndorId'].value}
    for tag in list(self.tags.values()):
        code = tag.code
        if not 4864 < code < 5031:
            continue
        value = tag.value
        name = tag.name[5:] if len(tag.name) > 5 else tag.name
        result[name] = value
        del tags[tag.name]
    return result