def _get_task_statuses(task_ids, cluster):
    response = client.describe_tasks(tasks=task_ids, cluster=cluster)
    if response['failures'] != []:
        raise Exception('There were some failures:\n{0}'.format(response[
            'failures']))
    status_code = response['ResponseMetadata']['HTTPStatusCode']
    if status_code != 200:
        msg = 'Task status request received status code {0}:\n{1}'
        raise Exception(msg.format(status_code, response))
    return [t['lastStatus'] for t in response['tasks']]