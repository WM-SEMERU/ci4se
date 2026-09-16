def _connect_client(self):
    overlapped = OVERLAPPED()
    overlapped.hEvent = create_event()
    while True:
        success = windll.kernel32.ConnectNamedPipe(self.pipe_handle, byref(
            overlapped))
        if success:
            return
        last_error = windll.kernel32.GetLastError()
        if last_error == ERROR_IO_PENDING:
            yield From(wait_for_event(overlapped.hEvent))
            return
        else:
            raise Exception('connect failed with error code' + str(last_error))