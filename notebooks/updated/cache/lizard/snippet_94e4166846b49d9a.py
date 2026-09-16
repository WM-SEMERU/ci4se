def path(self, which=None):
    if which in ('build_pxe_default', 'clone', 'revision'):
        prefix = 'self' if which == 'clone' else 'base'
        return '{0}/{1}'.format(super(ConfigTemplate, self).path(prefix), which
            )
    return super(ConfigTemplate, self).path(which)