def router(name, args, kwargs, options, task=None, **kw):
    task = task or celery.tasks.get(name)
    if not task:
        return
    if task.route:
        queue = task.route.split('.', 1)[0]
        return {'queue': queue, 'routing_key': task.route}
    if task.default_queue:
        key = task.default_routing_key
        key = key or '{0.default_queue}.{0.name}'.format(task)
        return {'queue': task.default_queue, 'routing_key': key}
    elif task.default_routing_key:
        return {'routing_key': task.default_routing_key}