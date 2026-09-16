def create_port_channel(self, nexus_host, vpc_nbr):
    starttime = time.time()
    vpc_str = str(vpc_nbr)
    path_snip = snipp.PATH_ALL
    body_snip = snipp.BODY_ADD_PORT_CH % (vpc_str, vpc_str, vpc_str)
    self.send_edit_string(nexus_host, path_snip, body_snip)
    self._apply_user_port_channel_config(nexus_host, vpc_nbr)
    self.capture_and_print_timeshot(starttime, 'create_port_channel',
        switch=nexus_host)