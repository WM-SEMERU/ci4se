def path(self, which=None):
    if which in ('smart_class_parameters', 'smart_variables'):
        return '{0}/{1}'.format(super(PuppetClass, self).path(which='self'),
            which)
    return super(PuppetClass, self).path(which)