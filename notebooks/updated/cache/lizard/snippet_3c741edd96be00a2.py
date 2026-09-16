def health_check(self):
    api_response = 'Online'
    result = 'Health check on resource {}'.format(self._resource_name)
    try:
        health_check_flow = RunCommandFlow(self.cli_handler, self._logger)
        health_check_flow.execute_flow()
        result += ' passed.'
    except Exception as e:
        self._logger.exception(e)
        api_response = 'Error'
        result += ' failed.'
    try:
        self._api.SetResourceLiveStatus(self._resource_name, api_response,
            result)
    except Exception:
        self._logger.error('Cannot update {} resource status on portal'.
            format(self._resource_name))
    return result