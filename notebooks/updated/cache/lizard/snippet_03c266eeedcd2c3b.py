def oauth_url(client_id, permissions=None, server=None, redirect_uri=None):
    url = ('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot'
        .format(client_id))
    if permissions is not None:
        url = url + '&permissions=' + str(permissions.value)
    if server is not None:
        url = url + '&guild_id=' + server.id
    if redirect_uri is not None:
        from urllib.parse import urlencode
        url = url + '&response_type=code&' + urlencode({'redirect_uri':
            redirect_uri})
    return url