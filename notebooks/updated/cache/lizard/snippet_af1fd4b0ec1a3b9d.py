def add_text(self, text, *args, **kwargs):
    section_name = kwargs.pop('section', None)
    para, sp = self._preformat_text(text, *args, **kwargs)
    if section_name is None:
        relevant_list = self.story
    else:
        relevant_list = self.sections[section_name]
    relevant_list.append(para)
    relevant_list.append(sp)
    return