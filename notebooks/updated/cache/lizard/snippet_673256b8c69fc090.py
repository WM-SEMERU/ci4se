def load_checkers():
    for loader, name, _ in pkgutil.iter_modules([os.path.join(__path__[0],
        'checkers')]):
        loader.find_module(name).load_module(name)