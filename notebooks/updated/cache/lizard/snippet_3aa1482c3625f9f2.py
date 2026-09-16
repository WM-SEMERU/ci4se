def greenlet_report(self):
    self.report_worker(w=1)
    while True:
        try:
            self.report_worker()
        except Exception as e:
            self.log.error('When reporting: %s' % e)
        finally:
            time.sleep(self.config['report_interval'])