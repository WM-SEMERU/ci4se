def to_config(self):
    from ..dynamixel.controller import DxlController
    dxl_controllers = [c for c in self._controllers if isinstance(c,
        DxlController)]
    config = {}
    config['controllers'] = {}
    for i, c in enumerate(dxl_controllers):
        name = 'dxl_controller_{}'.format(i)
        config['controllers'][name] = {'port': c.io.port, 'sync_read': c.io
            ._sync_read, 'attached_motors': [m.name for m in c.motors]}
    config['motors'] = {}
    for m in self.motors:
        config['motors'][m.name] = {'id': m.id, 'type': m.model, 'offset':
            m.offset, 'orientation': 'direct' if m.direct else 'indirect',
            'angle_limit': m.angle_limit}
        if m.angle_limit == (0, 0):
            config['motors']['wheel_mode'] = True
    config['motorgroups'] = {}
    return config