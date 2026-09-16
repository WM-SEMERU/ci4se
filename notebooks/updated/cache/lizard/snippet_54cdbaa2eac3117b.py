def is_theme(self, name):
    return getattr(self.args, 'theme_' + name) or self.theme['name'] == name