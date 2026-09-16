def prepare_request(settings):
    settings['sp']['assertionConsumerService'] = {'url': web.ctx.homedomain +
        web.ctx.homepath + '/auth/callback/' + settings['id'], 'binding':
        'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST'}
    data = web.input()
    return {'https': 'on' if web.ctx.protocol == 'https' else 'off',
        'http_host': web.ctx.environ['SERVER_NAME'], 'server_port': web.ctx
        .environ['SERVER_PORT'], 'script_name': web.ctx.homepath,
        'get_data': data.copy(), 'post_data': data.copy(), 'query_string':
        web.ctx.query}