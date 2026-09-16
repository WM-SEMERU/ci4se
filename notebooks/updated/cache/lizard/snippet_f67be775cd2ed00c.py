def make_server(function, port, authkey, qsize=None):
    QueueManager.register('get_job_q', callable=partial(return_arg, Queue(
        maxsize=qsize)))
    QueueManager.register('get_result_q', callable=partial(return_arg,
        Queue(maxsize=qsize)))
    QueueManager.register('get_function', callable=partial(return_arg,
        function))
    QueueManager.register('q_closed', callable=partial(return_arg,
        SharedConst(False)))
    host = 'localhost' if os.name == 'nt' else ''
    manager = QueueManager(address=(host, port), authkey=authkey)
    manager.start()
    return manager