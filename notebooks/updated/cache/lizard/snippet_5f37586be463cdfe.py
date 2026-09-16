def clone(self, data=None, shared_data=True, new_type=None, link=True, *
    args, **overrides):
    params = dict(self.get_param_values())
    if new_type is None:
        clone_type = self.__class__
    else:
        clone_type = new_type
        new_params = new_type.params()
        params = {k: v for k, v in params.items() if k in new_params}
        if params.get('group') == self.params()['group'].default:
            params.pop('group')
    settings = dict(params, **overrides)
    if 'id' not in settings:
        settings['id'] = self.id
    if data is None and shared_data:
        data = self.data
        if link:
            settings['plot_id'] = self._plot_id
    pos_args = getattr(self, '_' + type(self).__name__ + '__pos_params', [])
    return clone_type(data, *args, **{k: v for k, v in settings.items() if 
        k not in pos_args})