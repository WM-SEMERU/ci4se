def get_task_module(feature):
    try:
        importlib.import_module(feature)
    except ImportError:
        raise FeatureNotFound(feature)
    tasks_module = None
    try:
        tasks_module = importlib.import_module(feature + '.apetasks')
    except ImportError:
        pass
    try:
        tasks_module = importlib.import_module(feature + '.tasks')
    except ImportError:
        pass
    return tasks_module