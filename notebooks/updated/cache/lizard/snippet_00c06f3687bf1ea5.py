def maintainer(self):
    maintainer = namedtuple('Maintainer', 'name email')
    return maintainer(name=self._package['maintainer'], email=self._package
        ['maintainer_email'])