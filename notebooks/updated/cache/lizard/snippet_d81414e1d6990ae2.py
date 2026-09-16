def call(subcommand, args):
    args['<napp>'] = parse_napps(args['<napp>'])
    func = getattr(NAppsAPI, subcommand)
    func(args)