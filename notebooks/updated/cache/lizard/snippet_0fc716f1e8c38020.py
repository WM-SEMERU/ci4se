def collected(self, group, filename=None, host=None, location=None, move=
    True, all=True):
    ret = {'name': 'support.collected', 'changes': {}, 'result': True,
        'comment': ''}
    location = location or tempfile.gettempdir()
    self.check_destination(location, group)
    ret['changes'] = __salt__['support.sync'](group, name=filename, host=
        host, location=location, move=move, all=all)
    return ret