def main(directories):
    msg = 'Checking module "{}" from directory "{}" for coding errors.'
    api_checker = ApiChecker()
    resource_checker = ResourceChecker()
    errors = []
    modules = []
    for loader, mname, _ in pkgutil.walk_packages(directories):
        sys.path.append(os.path.abspath(loader.path))
        log.info(msg.format(mname, loader.path))
        modules.append(mname)
        import_module(mname)
    for api in Api:
        if api.__module__.split('.')[-1] not in modules:
            continue
        log.debug('Anlysing Api class: {}'.format(api.__name__))
        errors.extend(api_checker(api))
    for res in Resource:
        if res.__module__.split('.')[-1] not in modules:
            continue
        log.debug('Anlysing Resource class: {}'.format(res.__name__))
        errors.extend(resource_checker(res))
    else:
        log.info('All modules tested, no problem detected.')
    return errors