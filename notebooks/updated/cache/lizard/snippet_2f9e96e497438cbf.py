def vrrpe_spf_basic(self, **kwargs):
    int_type = kwargs.pop('int_type').lower()
    name = kwargs.pop('name')
    vrid = kwargs.pop('vrid')
    enable = kwargs.pop('enable', True)
    get = kwargs.pop('get', False)
    rbridge_id = kwargs.pop('rbridge_id', '1')
    callback = kwargs.pop('callback', self._callback)
    valid_int_types = ['gigabitethernet', 'tengigabitethernet',
        'fortygigabitethernet', 'hundredgigabitethernet', 'port_channel', 've']
    vrrpe_args = dict(name=name, vrid=vrid)
    method_class = self._interface
    if get:
        enable = None
    if int_type not in valid_int_types:
        raise ValueError('`int_type` must be one of: %s' % repr(
            valid_int_types))
    method_name = 'interface_%s_vrrpe_short_path_forwarding_basic' % int_type
    if int_type == 've':
        method_name = 'rbridge_id_%s' % method_name
        method_class = self._rbridge
        vrrpe_args['rbridge_id'] = rbridge_id
        if not pynos.utilities.valid_vlan_id(name):
            raise InvalidVlanId('`name` must be between `1` and `8191`')
    elif not pynos.utilities.valid_interface(int_type, name):
        raise ValueError(
            '`name` must be in the format of x/y/z for physical interfaces or x for port channel.'
            )
    vrrpe_spf_basic = getattr(method_class, method_name)
    config = vrrpe_spf_basic(**vrrpe_args)
    if get:
        return callback(config, handler='get_config')
    if not enable:
        config.find('.//*short-path-forwarding').set('operation', 'delete')
    return callback(config)