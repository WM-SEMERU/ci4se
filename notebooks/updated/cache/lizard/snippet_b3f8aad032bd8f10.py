def toggle_standby(self, **kwargs):
    trafficgroup = kwargs.pop('trafficgroup')
    state = kwargs.pop('state')
    if kwargs:
        raise TypeError('Unexpected **kwargs: %r' % kwargs)
    arguments = {'standby': state, 'traffic-group': trafficgroup}
    return self.exec_cmd('run', **arguments)