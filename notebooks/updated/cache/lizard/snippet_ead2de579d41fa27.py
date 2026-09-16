def initialize_block(self, block_header):
    state_view = BlockWrapper.state_view_for_block(self._block_cache.
        block_store.chain_head, self._state_view_factory)
    settings_view = SettingsView(state_view)
    self._min_wait_time = settings_view.get_setting(
        'sawtooth.consensus.min_wait_time', self._min_wait_time, int)
    self._max_wait_time = settings_view.get_setting(
        'sawtooth.consensus.max_wait_time', self._max_wait_time, int)
    self._valid_block_publishers = settings_view.get_setting(
        'sawtooth.consensus.valid_block_publishers', self.
        _valid_block_publishers, list)
    block_header.consensus = b'Devmode'
    self._start_time = time.time()
    self._wait_time = random.uniform(self._min_wait_time, self._max_wait_time)
    return True