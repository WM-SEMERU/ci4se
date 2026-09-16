def put_task_info(self, task_name, key, value):
    params = OrderedDict([('info', ''), ('taskname', task_name)])
    headers = {'Content-Type': 'application/xml'}
    body = self.TaskInfo(key=key, value=value).serialize()
    self._client.put(self.resource(), params=params, headers=headers, data=body
        )