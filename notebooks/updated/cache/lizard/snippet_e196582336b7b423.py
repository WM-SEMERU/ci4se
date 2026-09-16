def fabric_isl(self, **kwargs):
    int_type = str(kwargs.pop('int_type').lower())
    name = str(kwargs.pop('name'))
    enabled = kwargs.pop('enabled', True)
    callback = kwargs.pop('callback', self._callback)
    int_types = ['tengigabitethernet', 'fortygigabitethernet',
        'hundredgigabitethernet']
    if int_type not in int_types:
        raise ValueError('`int_type` must be one of: %s' % repr(int_types))
    if not isinstance(enabled, bool):
        raise ValueError('`enabled` must be `True` or `False`.')
    fabric_isl_args = dict(name=name)
    if not pynos.utilities.valid_interface(int_type, name):
        raise ValueError(
            '`name` must match `^[0-9]{1,3}/[0-9]{1,3}/[0-9]{1,3}$`')
    config = getattr(self._interface, 
        'interface_%s_fabric_fabric_isl_fabric_isl_enable' % int_type)(**
        fabric_isl_args)
    if not enabled:
        fabric_isl = config.find('.//*fabric-isl')
        fabric_isl.set('operation', 'delete')
    if kwargs.pop('get', False):
        return callback(config, handler='get_config')
    else:
        return callback(config)