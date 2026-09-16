def wait_for_connection(self, timeout=10):
    start_time = datetime.datetime.now()
    while True:
        if self.connected:
            return True
        now = datetime.datetime.now()
        if (now - start_time).total_seconds() > timeout:
            return False
        time.sleep(0.5)