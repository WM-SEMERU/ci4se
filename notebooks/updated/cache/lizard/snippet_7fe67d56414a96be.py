def monitor(self, job_id, timeout=5):
    while True:
        status = self.status(job_id)
        logging.info('Monitoring job: %d - Status: %d, %s' % (job_id,
            status[0], status[1]))
        if status[0] in [3, 4, 5]:
            return status
        time.sleep(timeout)