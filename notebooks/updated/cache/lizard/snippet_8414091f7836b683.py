def exec_cmd(self, command, **kwargs):
    self._is_allowed_command(command)
    self._check_command_parameters(**kwargs)
    if command == 'load':
        kwargs['command'] = command
        self._check_exclusive_parameters(**kwargs)
        requests_params = self._handle_requests_params(kwargs)
        session = self._meta_data['bigip']._meta_data['icr_session']
        try:
            session.post(self._meta_data['uri'], json=kwargs, **requests_params
                )
        except HTTPError as err:
            if err.response.status_code != 502:
                raise
            return
    else:
        return self._exec_cmd(command, **kwargs)