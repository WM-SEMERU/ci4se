def disconnect(self):
    try:
        self.cleanup()
        if self.protocol == 'ssh':
            self.paramiko_cleanup()
        elif self.protocol == 'telnet':
            self.remote_conn.close()
        elif self.protocol == 'serial':
            self.remote_conn.close()
    except Exception:
        pass
    finally:
        self.remote_conn_pre = None
        self.remote_conn = None
        self.close_session_log()