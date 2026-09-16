def get_css_background(self, uncomment=False, **kwargs):
    text = self._css_background(**kwargs)
    if uncomment:
        text = ' */ {} /* '.format(text)
    return text