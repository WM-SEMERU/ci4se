def get_input_column_attributes(self, extra_classes=None):
    all_classes = []
    css_class = self.input_column_class
    if css_class:
        all_classes.append(css_class)
    if extra_classes:
        all_classes.append(extra_classes)
    style = self.input_column_style
    parts = []
    if all_classes:
        parts.append('class="{}"'.format(' '.join(all_classes)))
    if style:
        parts.append('style="{}"'.format(style))
    return Markup(' '.join(parts))