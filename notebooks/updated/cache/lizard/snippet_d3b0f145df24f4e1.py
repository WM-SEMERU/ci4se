def waiting_member_state(self, timeout=300):
    t_start = time.time()
    while not self.check_member_state():
        if time.time() - t_start > timeout:
            return False
        time.sleep(0.1)
    return True