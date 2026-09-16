def __do_query_state(self):
    self._lutron.send(Lutron.OP_QUERY, Keypad._CMD_TYPE, self._keypad.id,
        self.component_number, Led._ACTION_LED_STATE)