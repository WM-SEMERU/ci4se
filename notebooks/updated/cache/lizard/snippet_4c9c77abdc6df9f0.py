def get_default(self):
    if self._overridden_default:
        if callable(self.default):
            default = self.default()
        else:
            default = self.default
    else:
        default = getattr(settings, 'PAGE_MENU_TEMPLATES_DEFAULT', None)
        if default is None:
            choices = self.get_choices(include_blank=False)
            default = (c[0] for c in choices)
    return tuple(default)