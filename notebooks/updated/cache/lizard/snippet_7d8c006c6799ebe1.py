def path(self, which=None):
    if which in ('cancel',):
        return '{0}/{1}'.format(super(RecurringLogic, self).path(which=
            'self'), which)
    return super(RecurringLogic, self).path(which)