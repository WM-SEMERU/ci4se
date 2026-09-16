def content_children(self):
    text_types = {CT_RegularTextRun, CT_TextLineBreak, CT_TextField}
    return tuple(elm for elm in self if type(elm) in text_types)