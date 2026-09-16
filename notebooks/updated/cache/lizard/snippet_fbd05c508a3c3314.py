def check_error(self):
    if not self.is_done:
        raise CloudUnhandledError(
            'Need to check if request is done, before checking for error')
    response = self.db[self.async_id]
    error_msg = response['error']
    status_code = int(response['status_code'])
    payload = response['payload']
    return status_code, error_msg, payload