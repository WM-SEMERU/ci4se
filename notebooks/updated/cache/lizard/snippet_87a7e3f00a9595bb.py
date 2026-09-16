def help_me(parser, opt):
    print('aomi v%s' % version)
    print('Get started with aomi https://autodesk.github.io/aomi/quickstart')
    if opt.verbose == 2:
        tf_str = 'Token File,' if token_file() else ''
        app_str = 'AppID File,' if appid_file() else ''
        approle_str = 'Approle File,' if approle_file() else ''
        tfe_str = 'Token Env,' if 'VAULT_TOKEN' in os.environ else ''
        appre_str = ('App Role Env,' if 'VAULT_ROLE_ID' in os.environ and 
            'VAULT_SECRET_ID' in os.environ else '')
        appe_str = ('AppID Env,' if 'VAULT_USER_ID' in os.environ and 
            'VAULT_APP_ID' in os.environ else '')
        LOG.info(('Auth Hints Present : %s%s%s%s%s%s' % (tf_str, app_str,
            approle_str, tfe_str, appre_str, appe_str))[:-1])
        LOG.info('Vault Server %s' % os.environ['VAULT_ADDR'] if 
            'VAULT_ADDR' in os.environ else '??')
    parser.print_help()
    sys.exit(0)