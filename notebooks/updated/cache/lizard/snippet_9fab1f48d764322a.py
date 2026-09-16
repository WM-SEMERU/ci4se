def package(self):
    if self.method == 'buildNotification':
        return self.params[1]['name']
    if self.method in ('createImage', 'image', 'livecd'):
        return self.params[0]
    if self.method == 'indirectionimage':
        return self.params[0]['name']
    if self.method not in ('build', 'buildArch', 'buildContainer',
        'buildMaven', 'buildSRPMFromSCM', 'maven'):
        return None
    source = self.params[0]
    o = urlparse(source)
    if source.endswith('.src.rpm'):
        srpm = os.path.basename(source)
        name, version, release = srpm.rsplit('-', 2)
        return name
    elif o.scheme:
        package = os.path.basename(o.path)
        if package.endswith('.git'):
            package = package[:-4]
        if self.method == 'buildContainer':
            package += '-container'
        return package
    raise ValueError('could not parse source "%s"' % source)