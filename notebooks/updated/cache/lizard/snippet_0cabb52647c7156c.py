def check_auth(args, role=None):
    users = boto3.resource('dynamodb').Table(os.environ['people'])
    if not (args.get('email', None) and args.get('api_key', None)):
        mesg = 'Invalid request: `email` and `api_key` are required'
        return {'success': False, 'message': mesg}
    user = users.get_item(Key={'email': args.get('email')})
    if 'Item' not in user:
        return {'success': False, 'message': 'User does not exist.'}
    user = user['Item']
    if user['api_key'] != args['api_key']:
        return {'success': False, 'message': 'API key was invalid.'}
    if role:
        if user['role'] not in role:
            mesg = 'User is not authorized to make this change.'
            return {'success': False, 'message': mesg}
    return {'success': True, 'message': None, 'user': user}