def work():
    with rq.Connection(create_connection()):
        worker = rq.Worker(list(map(rq.Queue, listen)))
        worker.work()