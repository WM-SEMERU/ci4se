def pause(self, instance_id, keep_provisioned=True):
    try:
        if self._paused:
            log.debug('node %s is already paused', instance_id)
            return
        self._paused = True
        post_shutdown_action = ('Stopped' if keep_provisioned else
            'StoppedDeallocated')
        result = self._subscription._sms.shutdown_role(service_name=self.
            _cloud_service._name, deployment_name=self._cloud_service._name,
            role_name=self._qualified_name, post_shutdown_action=
            post_shutdown_action)
        self._subscription._wait_result(result)
    except Exception as exc:
        log.error('error pausing instance %s: %s', instance_id, exc)
        raise
    log.debug('paused instance(instance_id=%s)', instance_id)