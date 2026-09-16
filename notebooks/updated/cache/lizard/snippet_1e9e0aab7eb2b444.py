def restore(self, volume_id, **kwargs):
    self.required('create', kwargs, ['backup', 'size'])
    volume_id = volume_id or str(uuid.uuid4())
    kwargs['volume_type_name'] = kwargs['volume_type_name'] or 'vtype'
    kwargs['size'] = kwargs['size'] or 1
    return self.http_put('/volumes/%s' % volume_id, params=self.unused(kwargs))