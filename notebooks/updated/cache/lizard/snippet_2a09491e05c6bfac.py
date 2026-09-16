def send_script_sync(self, conn_id, data, progress_callback):
    done = threading.Event()
    result = {}

    def send_script_done(conn_id, adapter_id, status, reason):
        result['success'] = status
        result['failure_reason'] = reason
        done.set()
    self.send_script_async(conn_id, data, progress_callback, send_script_done)
    done.wait()
    return result