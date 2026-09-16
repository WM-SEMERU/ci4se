def cmd_list(unused_conf: Config):
    for name, builder in sorted(Plugin.builders.items()):
        if builder.func:
            print('+- {0:16s} implemented in {1.__module__}.{1.__name__}()'
                .format(name, builder.func))
        else:
            print('+- {0:16s} loaded with no builder function'.format(name))
        for hook_name, hook_func in sorted(Plugin.get_hooks_for_builder(name)):
            print('  +- {0} hook implemented in {1.__module__}.{1.__name__}()'
                .format(hook_name, hook_func))