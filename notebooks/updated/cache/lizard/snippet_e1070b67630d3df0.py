def grant_user(userid, vswitch_name):
    print('\nGranting user %s ...' % userid)
    user_grant_info = client.send_request('vswitch_grant_user',
        vswitch_name, userid)
    if user_grant_info['overallRC']:
        raise RuntimeError('Failed to grant user %s!' % userid)
    else:
        print('Succeeded to grant user %s!' % userid)