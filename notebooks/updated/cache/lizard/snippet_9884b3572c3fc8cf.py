def load_plugins_dir(path, category=None, overwrite=False):
    if hasattr(path, 'glob'):
        pypaths = path.glob('*.py')
    else:
        pypaths = glob.glob(os.path.join(path, '*.py'))
    load_errors = []
    for pypath in pypaths:
        mod_name = str(uuid.uuid4())
        try:
            if hasattr(pypath, 'resolve'):
                pypath = pypath.resolve()
            with warnings.catch_warnings(record=True):
                warnings.filterwarnings('ignore', category=ImportWarning)
                if hasattr(pypath, 'maketemp'):
                    with pypath.maketemp() as f:
                        module = load_source(mod_name, f.name)
                else:
                    module = load_source(mod_name, str(pypath))
        except Exception as err:
            load_errors.append((str(pypath), 'Load Error: {}'.format(err)))
            continue
        class_members = inspect.getmembers(module, inspect.isclass)
        classes = [klass for klass_name, klass in class_members if klass.
            __module__ == mod_name]
        load_errors += load_plugin_classes(classes, category, overwrite)
    return load_errors