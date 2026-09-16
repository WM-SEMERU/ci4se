def set(args):
    from . import config, tweak


    class ConfigSaver(tweak.Config):

        @property
        def config_files(self):
            return [config.config_files[2]]
    config_saver = ConfigSaver(use_yaml=True, save_on_exit=False)
    c = config_saver
    for key in args.key.split('.')[:-1]:
        try:
            c = c[key]
        except KeyError:
            c[key] = {}
            c = c[key]
    c[args.key.split('.')[-1]] = json.loads(args.value
        ) if args.json else args.value
    config_saver.save()