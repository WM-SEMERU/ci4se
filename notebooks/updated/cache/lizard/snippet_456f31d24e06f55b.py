def sync(self):
    LOGGER.debug('IPAddress.sync')
    params = None
    if self.id is not None:
        params = {'id': self.id}
    elif self.ip_address is not None:
        params = {'ipAddress': self.ip_address}
    if params is not None:
        args = {'http_operation': 'GET', 'operation_path': 'get',
            'parameters': params}
        response = IPAddressService.requester.call(args)
        if response.rc != 0:
            LOGGER.warning(
                'IPAddress.sync - Problem while syncing IP address (name:' +
                self.ip_address + ', id: ' + str(self.id) + '). Reason: ' +
                str(response.response_content) + '-' + str(response.
                error_message) + ' (' + str(response.rc) + ')')
        else:
            json_obj = response.response_content
            self.id = json_obj['ipAddressID']
            self.ip_address = json_obj['ipAddressIPA']
            self.fqdn = json_obj['ipAddressFQDN']
            self.ipa_os_instance_id = json_obj['ipAddressOSInstanceID']
            self.ipa_subnet_id = json_obj['ipAddressSubnetID']