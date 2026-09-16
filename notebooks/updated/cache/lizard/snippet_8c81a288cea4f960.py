def upload_not_registered_user_data(data):
    if type(data) != dict:
        raise NotImplementedError('Incorrect data type')
    if not data.get('email'):
        raise KeyError('user_id as user.intercom_id or email is required')
    if not getattr(settings, 'SKIP_INTERCOM', False):
        intercom_data = {'email': data.get('email'), 'name': data.get(
            'name'), 'last_request_at': now().strftime('%s')}
        del data['email']
        if data.get('name'):
            del data['name']
        if data:
            intercom_data['custom_attributes'] = data
        try:
            intercom.users.create(**intercom_data)
        except errors.ServiceUnavailableError:
            pass