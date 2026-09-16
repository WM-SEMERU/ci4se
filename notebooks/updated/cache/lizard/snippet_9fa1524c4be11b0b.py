def tag(self, name, attrs=None, selfclosing=None):
    if self.disable_tags > 0:
        return
    if name in self.linkable_tags and attrs and len(attrs) > 0:
        for attrib in attrs:
            if attrib[0] in self.linkable_attrs:
                attrib[1] = INTERNAL_LINK.sub('{\\g<1>}', attrib[1])
    super().tag(name, attrs, selfclosing)