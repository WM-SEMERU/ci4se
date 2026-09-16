def color_stream_mt(istream=sys.stdin, n=config.N_PROCESSES, **kwargs):
    queue = multiprocessing.Queue(1000)
    lock = multiprocessing.Lock()
    pool = [multiprocessing.Process(target=color_process, args=(queue, lock
        ), kwargs=kwargs) for i in range(n)]
    for p in pool:
        p.start()
    block = []
    for line in istream:
        block.append(line.strip())
        if len(block) == config.BLOCK_SIZE:
            queue.put(block)
            block = []
    if block:
        queue.put(block)
    for i in range(n):
        queue.put(config.SENTINEL)
    for p in pool:
        p.join()