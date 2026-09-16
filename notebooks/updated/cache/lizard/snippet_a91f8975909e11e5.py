def path(self, which=None):
    if which in ('incremental_update', 'promote'):
        prefix = 'base' if which == 'incremental_update' else 'self'
        return '{0}/{1}'.format(super(ContentViewVersion, self).path(prefix
            ), which)
    return super(ContentViewVersion, self).path(which)