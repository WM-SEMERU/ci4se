def get_style_code(self, label):
    for style in self.styles:
        if style[0] == label:
            return style[1]
    msg = _('Label {label} is invalid.').format(label=label)
    raise ValueError(msg)