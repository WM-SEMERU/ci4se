def as_dict(self):
    info = {}
    info['type'] = self.__class__.__name__
    info['help'] = self.help
    info['default'] = self.default
    info['multi'] = self.multi
    info['uniq'] = self.uniq
    info['choices'] = self.choices
    return info