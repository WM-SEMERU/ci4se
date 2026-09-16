def call_actions_future(self, service_name, actions, expansions=None,
    raise_job_errors=True, raise_action_errors=True, timeout=None, **kwargs):
    kwargs.pop('suppress_response', None)
    if timeout:
        kwargs['message_expiry_in_seconds'] = timeout
    expected_request_id = self.send_request(service_name, actions, **kwargs)

    def get_response(_timeout=None):
        responses = list(self.get_all_responses(service_name,
            receive_timeout_in_seconds=_timeout or timeout))
        found = False
        response = None
        for request_id, response in responses:
            if request_id == expected_request_id:
                found = True
                break
        if not found:
            raise Exception(
                'Got unexpected response(s) with ID(s) {} for request with ID {}'
                .format([r[0] for r in responses], expected_request_id))
        if response.errors and raise_job_errors:
            raise self.JobError(response.errors)
        if raise_action_errors:
            error_actions = [action for action in response.actions if
                action.errors]
            if error_actions:
                raise self.CallActionError(error_actions)
        if expansions:
            kwargs.pop('continue_on_error', None)
            self._perform_expansion(response.actions, expansions, **kwargs)
        return response
    return self.FutureResponse(get_response)