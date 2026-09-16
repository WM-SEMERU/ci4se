def wait(self, interval=SGE_WAIT):
    finished = False
    while not finished:
        time.sleep(interval)
        interval = min(2 * interval, 60)
        finished = os.system('qstat -j %s > /dev/null' % self.name)