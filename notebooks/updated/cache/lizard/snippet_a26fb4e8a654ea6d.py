def info(self):
    info = self.get_params()
    info.update({'term_type': self._name})
    return info