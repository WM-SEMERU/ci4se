def worker(qin, qout, f):
    while not qin.empty():
        i, args = qin.get()
        qout.put((i, f(**args)))