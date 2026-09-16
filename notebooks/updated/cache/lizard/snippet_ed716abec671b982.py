def write(pylist, parallel=True):
    threads = [VSGWriter(o) for o in pylist]
    if parallel:
        for t in threads:
            t.start()
        for t in threads:
            t.join()
    else:
        for t in threads:
            t.run()