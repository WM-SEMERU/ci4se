def main():
    if len(sys.argv) < 2:
        print('Usage: {} SCOPE...'.format(sys.argv[0]))
        return 1
    authenticator = prawcore.TrustedAuthenticator(prawcore.Requestor(
        'prawcore_refresh_token_example'), os.environ['PRAWCORE_CLIENT_ID'],
        os.environ['PRAWCORE_CLIENT_SECRET'], os.environ[
        'PRAWCORE_REDIRECT_URI'])
    state = str(random.randint(0, 65000))
    url = authenticator.authorize_url('permanent', sys.argv[1:], state)
    print(url)
    client = receive_connection()
    data = client.recv(1024).decode('utf-8')
    param_tokens = data.split(' ', 2)[1].split('?', 1)[1].split('&')
    params = {key: value for key, value in [token.split('=') for token in
        param_tokens]}
    if state != params['state']:
        send_message(client, 'State mismatch. Expected: {} Received: {}'.
            format(state, params['state']))
        return 1
    elif 'error' in params:
        send_message(client, params['error'])
        return 1
    authorizer = prawcore.Authorizer(authenticator)
    authorizer.authorize(params['code'])
    send_message(client, 'Refresh token: {}'.format(authorizer.refresh_token))
    return 0