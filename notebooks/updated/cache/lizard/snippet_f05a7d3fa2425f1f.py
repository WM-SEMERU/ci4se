def _leave_handler(self, event):
    iid = self.current_iid
    if iid is None or self.active == iid:
        return
    self.update_state(iid, 'normal')