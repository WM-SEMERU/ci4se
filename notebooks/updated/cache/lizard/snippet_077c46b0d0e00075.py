def setup_kojiclient(profile):
    opts = koji.read_config(profile)
    for k, v in opts.iteritems():
        opts[k] = os.path.expanduser(v) if type(v) is str else v
    kojiclient = koji.ClientSession(opts['server'], opts=opts)
    kojiclient.ssl_login(opts['cert'], None, opts['serverca'])
    return kojiclient