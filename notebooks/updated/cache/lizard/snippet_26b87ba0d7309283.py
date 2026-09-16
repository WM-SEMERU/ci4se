def wait(self):
    while True:
        if not self.greenlet_watch:
            break
        if self.stopping:
            gevent.sleep(0.1)
        else:
            gevent.sleep(1)