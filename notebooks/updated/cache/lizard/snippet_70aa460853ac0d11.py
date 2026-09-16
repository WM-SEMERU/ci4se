def list_surveys(session):
    params = {'sUser': session['user'], 'sSessionKey': session['token']}
    data = set_params('list_surveys', params)
    req = requests.post(session['url'], data=data, headers=headers)
    return req.text