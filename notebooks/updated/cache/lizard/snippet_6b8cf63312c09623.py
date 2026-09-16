def path(self, which=None):
    if which in ('add_subscriptions', 'remove_subscriptions'):
        return '{0}/{1}'.format(super(HostSubscription, self).path(which=
            'base'), which)
    return super(HostSubscription, self).path(which)