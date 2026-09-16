def status(self):
    transfered = self.download - self.prev_download
    now = time.time()
    interval = now - self.last_status_time
    self.last_status_time = now
    return (
        'DFLogger: %(state)s Rate(%(interval)ds):%(rate).3fkB/s Block:%(block_cnt)d Missing:%(missing)d Fixed:%(fixed)d Abandoned:%(abandoned)d'
         % {'interval': interval, 'rate': transfered / (interval * 1000),
        'block_cnt': self.block_cnt, 'missing': len(self.missing_blocks),
        'fixed': self.missing_found, 'abandoned': self.abandoned, 'state': 
        'Inactive' if self.stopped else 'Active'})