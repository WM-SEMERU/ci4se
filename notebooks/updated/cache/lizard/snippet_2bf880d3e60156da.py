def get_proc_title(self):
    has_worker = bool(getattr(self, 'worker', None))
    title_parts = [self.prog_name.replace('.py', '#%s' % self.worker.id if
        has_worker else '')]
    status = 'init'
    if has_worker and self.worker.status:
        status = self.worker.status
        if self.worker.end_forced:
            status += ' - ending'
    title_parts.append('[%s]' % status)
    if has_worker and self.worker.queues:
        title_parts.append('queues=%s' % ','.join(self.worker.queues))
    if has_worker and self.worker.status:
        title_parts.append('loop=%s/%s' % (self.worker.num_loops, self.
            worker.max_loops))
        title_parts.append('waiting=%s' % self.worker.count_waiting_jobs())
        title_parts.append('delayed=%s' % self.worker.count_delayed_jobs())
        if self.worker.start_date:
            duraiton_message = 'duration=%s'
            duration_args = timedelta(seconds=int(round(self.worker.elapsed
                .total_seconds()))),
            if self.worker.max_duration:
                duraiton_message += '/%s'
                duration_args += self.worker.max_duration,
            title_parts.append(duraiton_message % duration_args)
    return ' '.join(title_parts)