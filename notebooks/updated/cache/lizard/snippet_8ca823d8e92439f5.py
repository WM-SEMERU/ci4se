def poll(self):
    if not self.pod_reflector.first_load_future.done():
        yield self.pod_reflector.first_load_future
    data = self.pod_reflector.pods.get(self.pod_name, None)
    if data is not None:
        if data.status.phase == 'Pending':
            return None
        ctr_stat = data.status.container_statuses
        if ctr_stat is None:
            return 1
        for c in ctr_stat:
            if c.name == 'notebook':
                if c.state.terminated:
                    if self.delete_stopped_pods:
                        yield self.stop(now=True)
                    return c.state.terminated.exit_code
                break
        return None
    return 1