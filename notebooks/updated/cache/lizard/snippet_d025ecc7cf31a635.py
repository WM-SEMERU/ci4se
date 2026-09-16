def normalize_path():
    whole_path = [os.path.abspath(path) for path in sys.path if os.path.
        exists(path)]
    whole_set = collections.OrderedDict((('', 1), (os.getcwd(), 1)))
    for path in whole_path:
        if path not in whole_set:
            whole_set[path] = 1
    sys.path = list(whole_set)
    for module_ in sys.modules.values():
        try:
            module_.__path__ = [os.path.abspath(path) for path in module_.
                __path__ if _package_exists(path)]
        except AttributeError:
            pass
        except ImportError:
            pass