def send_edit_string(self, nexus_host, path_snip, body_snip,
    check_to_close_session=True):
    starttime = time.time()
    LOG.debug('NexusDriver edit config for host %s: path: %s body: %s',
        nexus_host, path_snip, body_snip)
    self.client.rest_post(path_snip, nexus_host, body_snip)
    self.capture_and_print_timeshot(starttime, 'send_edit', switch=nexus_host)