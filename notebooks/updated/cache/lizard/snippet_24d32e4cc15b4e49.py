def _send_cli_conf_string(self, nexus_host, cli_str):
    starttime = time.time()
    path_snip = snipp.PATH_USER_CMDS
    body_snip = snipp.BODY_USER_CONF_CMDS % ('1', cli_str)
    LOG.debug('NexusDriver CLI config for host %s: path: %s body: %s',
        nexus_host, path_snip, body_snip)
    self.nxapi_client.rest_post(path_snip, nexus_host, body_snip)
    self.capture_and_print_timeshot(starttime, 'send_cliconf', switch=
        nexus_host)