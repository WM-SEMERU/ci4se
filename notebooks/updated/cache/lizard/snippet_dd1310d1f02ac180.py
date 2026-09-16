def get_user_details(self, response):
    result = {'id': response['id'], 'username': response.get('username',
        None), 'email': response.get('email', None), 'first_name': response
        .get('first_name', None), 'last_name': response.get('last_name', None)}
    if result['first_name'] and result['last_name']:
        result['fullname'] = result['first_name'] + ' ' + result['last_name']
    return result