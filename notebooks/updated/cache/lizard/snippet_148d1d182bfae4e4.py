def update_task(self, id, new_lease_time, client=None):
    client = self._require_client(client)
    task = Task(taskqueue=self, id=id)
    try:
        response = client.connection.api_request(method='POST', path=self.
            path + '/tasks/' + id, query_params={'newLeaseSeconds':
            new_lease_time}, _target_object=task)
        task._set_properties(response)
        return task
    except NotFound:
        return None