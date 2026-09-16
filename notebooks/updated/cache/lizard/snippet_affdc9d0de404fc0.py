def send_script_async(self, conn_id, data, progress_callback, callback):
    callback(conn_id, self.id, False,
        'Sending scripts is not supported by this device adapter')