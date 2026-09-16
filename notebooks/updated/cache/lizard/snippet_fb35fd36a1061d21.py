def _get_callback_context(env):
    if env.model is not None and env.cvfolds is None:
        context = 'train'
    elif env.model is None and env.cvfolds is not None:
        context = 'cv'
    return context