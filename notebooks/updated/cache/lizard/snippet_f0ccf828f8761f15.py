def _wait_for_process(self, p, shell=False):
    local_maxmem = -1
    sleeptime = 0.5
    while p.poll() is None:
        if not shell:
            local_maxmem = max(local_maxmem, self._memory_usage(p.pid) / 
                1000000.0)
        time.sleep(sleeptime)
        sleeptime = min(sleeptime + 5, 60)
    self.peak_memory = max(self.peak_memory, local_maxmem)
    del self.procs[p.pid]
    info = 'Process ' + str(p.pid) + ' returned: (' + str(p.returncode) + ').'
    if not shell:
        info += ' Peak memory: (Process: ' + str(round(local_maxmem, 3)
            ) + 'GB;'
        info += ' Pipeline: ' + str(round(self.peak_memory, 3)) + 'GB)\n'
    print(info + '\n')
    if p.returncode != 0:
        raise Exception('Process returned nonzero result.')
    return [p.returncode, local_maxmem]