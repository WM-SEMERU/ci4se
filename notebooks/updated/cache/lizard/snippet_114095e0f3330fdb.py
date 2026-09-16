def getPackages(self, distribution='rawhide'):
    if self._packages == {}:
        file_location = '%s/data/distribution_packages.json' % getScriptDir(
            __file__)
        with open(file_location, 'r') as f:
            packages = json.load(f)
        for pkg in packages:
            for distro in pkg['distributions']:
                try:
                    self._packages[distro].append(pkg['package'])
                except KeyError:
                    self._packages[distro] = [pkg['package']]
    return self._packages[distribution]