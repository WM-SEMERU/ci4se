def multiput(client, objs, **options):
    transient_pool = False
    outq = Queue()
    if 'pool' in options:
        pool = options['pool']
        del options['pool']
    else:
        pool = MultiPutPool()
        transient_pool = True
    try:
        pool.start()
        for obj in objs:
            task = PutTask(client, outq, obj, options)
            pool.enq(task)
        results = []
        for _ in range(len(objs)):
            if pool.stopped():
                raise RuntimeError(
                    'Multi-put operation interrupted by pool stopping!')
            results.append(outq.get())
            outq.task_done()
    finally:
        if transient_pool:
            pool.stop()
    return results