def scale(self, n):
    pods = self._cleanup_terminated_pods(self.pods())
    if n >= len(pods):
        return self.scale_up(n, pods=pods)
    else:
        n_to_delete = len(pods) - n
        running_workers = list(self.scheduler.workers.keys())
        running_ips = set(urlparse(worker).hostname for worker in
            running_workers)
        pending_pods = [p for p in pods if p.status.pod_ip not in running_ips]
        if pending_pods:
            pending_to_delete = pending_pods[:n_to_delete]
            logger.debug('Deleting pending pods: %s', pending_to_delete)
            self._delete_pods(pending_to_delete)
            n_to_delete = n_to_delete - len(pending_to_delete)
            if n_to_delete <= 0:
                return
        to_close = select_workers_to_close(self.scheduler, n_to_delete)
        logger.debug('Closing workers: %s', to_close)
        if len(to_close) < len(self.scheduler.workers):

            @gen.coroutine
            def f(to_close):
                yield self.scheduler.retire_workers(workers=to_close,
                    remove=True, close_workers=True)
                yield offload(self.scale_down, to_close)
            self.scheduler.loop.add_callback(f, to_close)
            return
        self.scale_down(to_close)