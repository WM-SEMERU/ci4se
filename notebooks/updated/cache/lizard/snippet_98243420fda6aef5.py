def load_states():
    states = {}
    __opts__['grains'] = salt.loader.grains(__opts__)
    __opts__['pillar'] = __pillar__
    lazy_utils = salt.loader.utils(__opts__)
    lazy_funcs = salt.loader.minion_mods(__opts__, utils=lazy_utils)
    lazy_serializers = salt.loader.serializers(__opts__)
    lazy_states = salt.loader.states(__opts__, lazy_funcs, lazy_utils,
        lazy_serializers)
    for key, func in six.iteritems(lazy_states):
        if '.' not in key:
            continue
        mod_name, func_name = key.split('.', 1)
        if mod_name not in states:
            states[mod_name] = {}
        states[mod_name][func_name] = func
    __context__['pyobjects_states'] = states