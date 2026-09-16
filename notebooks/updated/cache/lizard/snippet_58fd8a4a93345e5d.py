def get_classes(modName):
    classNames = []
    for name, obj in inspect.getmembers(sys.modules[modName]):
        if inspect.isclass(obj):
            classNames.append(name)
    return classNames