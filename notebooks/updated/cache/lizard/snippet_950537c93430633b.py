def system_info(conf, args):
    src = conf.config['instances'][args.src]
    src_url = api.build_system_url(build_instance_url(src))
    src_auth = tuple([conf.creds['instances'][args.src]['user'], conf.creds
        ['instances'][args.src]['pass']])
    verify_ssl = src.get('verify_ssl', True)
    sysinfo_json = api.system_info(src_url, src_auth, verify_ssl)
    return sysinfo_json