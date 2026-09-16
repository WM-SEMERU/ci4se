def add_style(self, name, style_type, builtin=False):
    style_name = BabelFish.ui2internal(name)
    if style_name in self:
        raise ValueError("document already contains style '%s'" % name)
    style = self._element.add_style_of_type(style_name, style_type, builtin)
    return StyleFactory(style)