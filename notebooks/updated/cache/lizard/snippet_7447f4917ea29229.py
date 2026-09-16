def collect(self, app_id, exp_config=None, bot=False, **kwargs):
    try:
        results = data_load(app_id)
        self.log('Data found for experiment {}, retrieving.'.format(app_id),
            key='Retrieve:')
        return results
    except IOError:
        self.log('Could not fetch data for id: {}, checking registry'.
            format(app_id), key='Retrieve:')
    exp_config = exp_config or {}
    if is_registered(app_id):
        raise RuntimeError('The id {} is registered, '.format(app_id) +
            'but you do not have permission to access to the data')
    elif kwargs.get('mode') == 'debug' or exp_config.get('mode') == 'debug':
        raise RuntimeError('No remote or local data found for id {}'.format
            (app_id))
    try:
        assert isinstance(uuid.UUID(app_id, version=4), uuid.UUID)
    except (ValueError, AssertionError):
        raise ValueError('Invalid UUID supplied {}'.format(app_id))
    self.log('{} appears to be a new experiment id, running experiment.'.
        format(app_id), key='Retrieve:')
    return self.run(exp_config, app_id, bot, **kwargs)