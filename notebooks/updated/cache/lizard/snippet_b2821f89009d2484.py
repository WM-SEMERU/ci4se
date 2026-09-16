def client_args_for_bank(bank_info, ofx_version):
    client_args = {'ofx_version': str(ofx_version)}
    if 'ofx.discovercard.com' in bank_info['url']:
        client_args['user_agent'] = False
        client_args['accept'] = False
    if 'www.accountonline.com' in bank_info['url']:
        client_args['user_agent'] = False
    return client_args