def upload(self, file_path, uri=None, timeout=-1):
    if not uri:
        uri = self._uri
    upload_file_name = os.path.basename(file_path)
    task, entity = self._connection.post_multipart_with_response_handling(uri,
        file_path, upload_file_name)
    if not task:
        return entity
    return self._task_monitor.wait_for_task(task, timeout)