def get_release_task_attachments(self, project, release_id, environment_id,
    attempt_id, plan_id, type):
    route_values = {}
    if project is not None:
        route_values['project'] = self._serialize.url('project', project, 'str'
            )
    if release_id is not None:
        route_values['releaseId'] = self._serialize.url('release_id',
            release_id, 'int')
    if environment_id is not None:
        route_values['environmentId'] = self._serialize.url('environment_id',
            environment_id, 'int')
    if attempt_id is not None:
        route_values['attemptId'] = self._serialize.url('attempt_id',
            attempt_id, 'int')
    if plan_id is not None:
        route_values['planId'] = self._serialize.url('plan_id', plan_id, 'str')
    if type is not None:
        route_values['type'] = self._serialize.url('type', type, 'str')
    response = self._send(http_method='GET', location_id=
        'a4d06688-0dfa-4895-82a5-f43ec9452306', version='5.0-preview.1',
        route_values=route_values)
    return self._deserialize('[ReleaseTaskAttachment]', self.
        _unwrap_collection(response))