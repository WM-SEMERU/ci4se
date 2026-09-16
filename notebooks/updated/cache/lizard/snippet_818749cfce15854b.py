def get(args):
    from . import config
    for key in args.key.split('.'):
        config = getattr(config, key)
    print(json.dumps(config))