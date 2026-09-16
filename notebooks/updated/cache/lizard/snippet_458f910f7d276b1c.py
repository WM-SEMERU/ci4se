def sync(self):
    LOGGER.debug('OSInstance.sync')
    params = None
    if self.id is not None:
        params = {'id': self.id}
    elif self.name is not None:
        params = {'name': self.name}
    if params is not None:
        args = {'http_operation': 'GET', 'operation_path': 'get',
            'parameters': params}
        response = OSInstanceService.requester.call(args)
        if response.rc != 0:
            LOGGER.warning(
                'OSInstance.sync - Problem while syncing OS instance (name:' +
                self.name + ', id:' + str(self.id) + '). Reason: ' + str(
                response.response_content) + '-' + str(response.
                error_message) + ' (' + str(response.rc) + ')')
        else:
            json_obj = response.response_content
            self.id = json_obj['osInstanceID']
            self.name = json_obj['osInstanceName']
            self.description = json_obj['osInstanceDescription']
            self.admin_gate_uri = json_obj['osInstanceAdminGateURI']
            if json_obj['osInstanceOSTypeID'] == -1:
                self.ost_id = None
            else:
                self.ost_id = json_obj['osInstanceOSTypeID']
            if json_obj['osInstanceEmbeddingOSInstanceID'] == -1:
                self.embedding_osi_id = None
            else:
                self.embedding_osi_id = json_obj[
                    'osInstanceEmbeddingOSInstanceID']
            self.embedded_osi_ids = json_obj['osInstanceEmbeddedOSInstancesID']
            self.ip_address_ids = json_obj['osInstanceIPAddressesID']
            self.nic_ids = json_obj['osInstanceNICsID']
            self.application_ids = json_obj['osInstanceApplicationsID']
            self.environment_ids = json_obj['osInstanceEnvironmentsID']
            self.subnet_ids = json_obj['osInstanceSubnetsID']
            self.team_ids = json_obj['osInstanceTeamsID']