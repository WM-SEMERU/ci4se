def factory(start_immediately=True):

    def decorator(func):

        def wrapper(*args, **kwargs):
            job = Job(task=lambda j: func(j, *args, **kwargs))
            if start_immediately:
                job.start()
            return job
        return wrapper
    return decorator