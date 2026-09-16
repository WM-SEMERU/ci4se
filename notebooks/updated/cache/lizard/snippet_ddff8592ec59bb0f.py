def load(cls, filename, namespace, loader_func, min_interval=0, comparators
    =None):
    watcher = ConfigurationWatcher(build_loader_callable(loader_func,
        filename, namespace=namespace), filename, min_interval=min_interval,
        reloader=ReloadCallbackChain(namespace=namespace), comparators=
        comparators)
    watcher.load_config()
    return cls(watcher)