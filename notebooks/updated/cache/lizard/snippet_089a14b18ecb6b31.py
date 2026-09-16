def switch_off(self):
    success = self.set_status(CONST.STATUS_OFF_INT)
    if success:
        self._json_state['status'] = CONST.STATUS_CLOSED
    return success