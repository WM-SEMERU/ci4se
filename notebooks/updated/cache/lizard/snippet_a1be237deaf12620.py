def taskException(self, *args, **kwargs):
    ref = {'exchange': 'task-exception', 'name': 'taskException',
        'routingKey': [{'constant': 'primary', 'multipleWords': False,
        'name': 'routingKeyKind'}, {'multipleWords': False, 'name':
        'taskId'}, {'multipleWords': False, 'name': 'runId'}, {
        'multipleWords': False, 'name': 'workerGroup'}, {'multipleWords':
        False, 'name': 'workerId'}, {'multipleWords': False, 'name':
        'provisionerId'}, {'multipleWords': False, 'name': 'workerType'}, {
        'multipleWords': False, 'name': 'schedulerId'}, {'multipleWords':
        False, 'name': 'taskGroupId'}, {'multipleWords': True, 'name':
        'reserved'}], 'schema': 'v1/task-exception-message.json#'}
    return self._makeTopicExchange(ref, *args, **kwargs)