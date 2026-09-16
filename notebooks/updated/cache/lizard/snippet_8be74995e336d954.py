def py_resources():
    aomi_mods = [m for m, _v in iteritems(sys.modules) if m.startswith(
        'aomi.model')]
    mod_list = []
    mod_map = []
    for amod in [sys.modules[m] for m in aomi_mods]:
        for _mod_bit, model in inspect.getmembers(amod):
            if str(model) in mod_list:
                continue
            if model == Mount:
                mod_list.append(str(model))
                mod_map.append((model.config_key, model))
            elif inspect.isclass(model) and issubclass(model, Resource
                ) and model.config_key:
                mod_list.append(str(model))
                if model.resource_key:
                    mod_map.append((model.config_key, model.resource_key,
                        model))
                elif model.config_key != 'secrets':
                    mod_map.append((model.config_key, model))
    return mod_map