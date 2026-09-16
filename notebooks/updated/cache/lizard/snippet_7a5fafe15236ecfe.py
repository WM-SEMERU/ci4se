def add_environment(self, environment, sync=True):
    LOGGER.debug('OSInstance.add_environment')
    if not sync:
        self.environment_2_add.append(environment)
    else:
        if environment.id is None:
            environment.save()
        if self.id is not None and environment.id is not None:
            params = {'id': self.id, 'environmentID': environment.id}
            args = {'http_operation': 'GET', 'operation_path':
                'update/environments/add', 'parameters': params}
            response = OSInstanceService.requester.call(args)
            if response.rc != 0:
                LOGGER.warning(
                    'OSInstance.add_environment - Problem while updating OS instance '
                     + self.name + '. Reason: ' + str(response.
                    response_content) + '-' + str(response.error_message) +
                    ' (' + str(response.rc) + ')')
            else:
                self.environment_ids.append(environment.id)
                environment.osi_ids.append(self.id)
        else:
            LOGGER.warning(
                'OSInstance.add_environment - Problem while updating OS instance '
                 + self.name + '. Reason: application ' + environment.name +
                ' id is None')