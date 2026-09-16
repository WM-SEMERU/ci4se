def lock(self):
    success = self.set_status(CONST.STATUS_LOCKCLOSED_INT)
    if success:
        self._json_state['status'] = CONST.STATUS_LOCKCLOSED
    return success