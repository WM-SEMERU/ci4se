def authorize(args):
    oauth2_instance = oauth2.build_oauth2(args.app, args)
    oauth2_instance.build_authorizer()
    logging.info('Application "%s" authorized!', args.app)