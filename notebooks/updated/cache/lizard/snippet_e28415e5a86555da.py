def start(self):
    w.setproctitle('oq-dbserver')
    dworkers = []
    for _ in range(self.num_workers):
        sock = z.Socket(self.backend, z.zmq.REP, 'connect')
        threading.Thread(target=self.dworker, args=(sock,)).start()
        dworkers.append(sock)
    logging.warning('DB server started with %s on %s, pid %d', sys.
        executable, self.frontend, self.pid)
    if ZMQ:
        c = config.zworkers
        threading.Thread(target=w._streamer, args=(self.master_host, c.
            task_in_port, c.task_out_port)).start()
        logging.warning('Task streamer started from %s -> %s', c.
            task_in_port, c.task_out_port)
        msg = self.master.start()
        logging.warning(msg)
        time.sleep(1)
    try:
        z.zmq.proxy(z.bind(self.frontend, z.zmq.ROUTER), z.bind(self.
            backend, z.zmq.DEALER))
    except (KeyboardInterrupt, z.zmq.ZMQError):
        for sock in dworkers:
            sock.running = False
            sock.zsocket.close()
        logging.warning('DB server stopped')
    finally:
        self.stop()