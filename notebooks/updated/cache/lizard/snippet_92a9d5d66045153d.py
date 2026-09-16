def spawn_process(self, target, *args):
    p = Process(target=target, args=args)
    p.daemon = True
    if target == worker:
        p.daemon = Conf.DAEMONIZE_WORKERS
        p.timer = args[2]
        self.pool.append(p)
    p.start()
    return p