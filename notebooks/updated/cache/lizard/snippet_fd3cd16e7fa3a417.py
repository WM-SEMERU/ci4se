def _new(self, dx_hash, close=False, **kwargs):
    if 'init_from' in kwargs:
        if kwargs['init_from'] is not None:
            if not isinstance(kwargs['init_from'], DXRecord):
                raise DXError('Expected instance of DXRecord to init_from')
            dx_hash['initializeFrom'] = {'id': kwargs['init_from'].get_id(),
                'project': kwargs['init_from'].get_proj_id()}
        del kwargs['init_from']
    if close:
        dx_hash['close'] = True
    resp = dxpy.api.record_new(dx_hash, **kwargs)
    self.set_ids(resp['id'], dx_hash['project'])