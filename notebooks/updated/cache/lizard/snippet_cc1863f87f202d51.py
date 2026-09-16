def deploy_ray_func(func, partition, kwargs):
    try:
        return func(partition, **kwargs)
    except ValueError:
        return func(partition.copy(), **kwargs)