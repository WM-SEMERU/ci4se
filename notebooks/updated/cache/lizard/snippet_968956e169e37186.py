def symlink_list(self, load):
    if 'env' in load:
        load.pop('env')
    ret = {}
    if 'saltenv' not in load:
        return {}
    if not isinstance(load['saltenv'], six.string_types):
        load['saltenv'] = six.text_type(load['saltenv'])
    for fsb in self.backends(load.pop('fsbackend', None)):
        symlstr = '{0}.symlink_list'.format(fsb)
        if symlstr in self.servers:
            ret = self.servers[symlstr](load)
    prefix = load.get('prefix', '').strip('/')
    if prefix != '':
        ret = dict([(x, y) for x, y in six.iteritems(ret) if x.startswith(
            prefix)])
    return ret