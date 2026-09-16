def session_preparation(self):
    delay_factor = self.select_delay_factor(delay_factor=0)
    i = 1
    while i <= 4:
        time.sleep(0.5 * delay_factor)
        self.write_channel('\n')
        i += 1
    time.sleep(0.3 * delay_factor)
    self.clear_buffer()
    self._test_channel_read(pattern='[>\\]]')
    self.set_base_prompt()
    command = self.RETURN + 'screen-length disable'
    self.disable_paging(command=command)
    time.sleep(0.3 * self.global_delay_factor)
    self.clear_buffer()