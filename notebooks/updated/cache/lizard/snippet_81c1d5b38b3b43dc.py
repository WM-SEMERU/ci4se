def _bfd_rx(self, **kwargs):
    int_type = kwargs['int_type']
    method_name = 'interface_%s_bfd_interval_min_rx' % int_type
    bfd_rx = getattr(self._interface, method_name)
    config = bfd_rx(**kwargs)
    if kwargs['delete']:
        tag = 'min-rx'
        config.find('.//*%s' % tag).set('operation', 'delete')
        pass
    return config