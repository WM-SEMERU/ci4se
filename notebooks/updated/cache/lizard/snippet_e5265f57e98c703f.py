def create(self, client=None):
    if self.notification_id is not None:
        raise ValueError('Notification already exists w/ id: {}'.format(
            self.notification_id))
    client = self._require_client(client)
    query_params = {}
    if self.bucket.user_project is not None:
        query_params['userProject'] = self.bucket.user_project
    path = '/b/{}/notificationConfigs'.format(self.bucket.name)
    properties = self._properties.copy()
    properties['topic'] = _TOPIC_REF_FMT.format(self.topic_project, self.
        topic_name)
    self._properties = client._connection.api_request(method='POST', path=
        path, query_params=query_params, data=properties)