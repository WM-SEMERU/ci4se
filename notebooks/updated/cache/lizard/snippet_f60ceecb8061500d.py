def wait_for_master_death(self):
    logger.info('Waiting for master death')
    timeout = 1.0
    self.last_master_ping = time.time()
    master_timeout = 300
    for arbiter_link in self.conf.arbiters:
        if not arbiter_link.spare:
            master_timeout = (arbiter_link.spare_check_interval *
                arbiter_link.spare_max_check_attempts)
    logger.info("I'll wait master death for %d seconds", master_timeout)
    while not self.interrupted:
        _, tcdiff = self.make_a_pause(timeout)
        if tcdiff:
            self.last_master_ping += tcdiff
        if self.new_conf:
            self.setup_new_conf()
        sys.stdout.write('.')
        sys.stdout.flush()
        now = time.time()
        if now - self.last_master_ping > master_timeout:
            logger.info(
                'Arbiter Master is dead. The arbiter %s takes the lead!',
                self.link_to_myself.name)
            for arbiter_link in self.conf.arbiters:
                if not arbiter_link.spare:
                    arbiter_link.alive = False
            self.must_run = True
            break