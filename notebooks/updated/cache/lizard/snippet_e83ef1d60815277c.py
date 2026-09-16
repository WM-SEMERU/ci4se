def restart(self, restart_only_stale_services=None,
    redeploy_client_configuration=None, restart_service_names=None):
    if self._get_resource_root().version < 6:
        return self._cmd('restart')
    else:
        args = dict()
        args['restartOnlyStaleServices'] = restart_only_stale_services
        args['redeployClientConfiguration'] = redeploy_client_configuration
        if self._get_resource_root().version >= 11:
            args['restartServiceNames'] = restart_service_names
        return self._cmd('restart', data=args, api_version=6)