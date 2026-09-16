def get_task(client, task_id):
    endpoint = '/'.join([client.api.Endpoints.TASKS, str(task_id)])
    response = client.authenticated_request(endpoint)
    return response.json()