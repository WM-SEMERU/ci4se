def del_application(self, application, sync=True):
    LOGGER.debug('OSInstance.del_application')
    if not sync:
        self.application_2_rm.append(application)
    else:
        if application.id is None:
            application.sync()
        if self.id is not None and application.id is not None:
            params = {'id': self.id, 'applicationID': application.id}
            args = {'http_operation': 'GET', 'operation_path':
                'update/applications/delete', 'parameters': params}
            response = OSInstanceService.requester.call(args)
            if response.rc != 0:
                LOGGER.warning(
                    'OSInstance.del_application - Problem while updating OS instance '
                     + self.name + '. Reason: ' + str(response.
                    response_content) + '-' + str(response.error_message) +
                    ' (' + str(response.rc) + ')')
            else:
                self.application_ids.remove(application.id)
                application.osi_ids.remove(self.id)
        else:
            LOGGER.warning(
                'OSInstance.del_application - Problem while updating OS instance '
                 + self.name + '. Reason: application ' + application.name +
                ' id is None')