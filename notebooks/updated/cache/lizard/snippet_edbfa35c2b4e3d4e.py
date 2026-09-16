def delete_subtask(client, subtask_id, revision):
    params = {'revision': int(revision)}
    endpoint = '/'.join([client.api.Endpoints.SUBTASKS, str(subtask_id)])
    client.authenticated_request(endpoint, 'DELETE', params=params)