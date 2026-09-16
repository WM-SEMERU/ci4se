def create_disposable(clientInfo, config={}):
    response = requests.put(_format_url(_extend(DEFAULT_CONFIG, config), 
        OAUTH2_ROOT + 'disposable'), json=clientInfo)
    if response.status_code != 200:
        return None
    else:
        body = response.json()
        return Blotre({'client_id': body['id'], 'client_secret': body[
            'secret'], 'code': body['code']}, config=config)