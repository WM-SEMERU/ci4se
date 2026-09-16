def get_livestate(self):
    livestate = 0
    if self.active:
        if not self.reachable:
            livestate = 1
        elif not self.alive:
            livestate = 2
    else:
        livestate = 3
    livestate_output = '%s/%s is %s' % (self.type, self.name, [
        'up and running.', 'warning because not reachable.',
        'critical because not responding.', 'not active by configuration.']
        [livestate])
    return livestate, livestate_output