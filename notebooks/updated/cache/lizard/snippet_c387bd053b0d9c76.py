def _execute_transactions(self, address):
    for i in range(self.transaction_count):
        self.time = datetime.now()
        log.info(
            'Starting message call transaction, iteration: {}, {} initial states'
            .format(i, len(self.open_states)))
        for hook in self._start_sym_trans_hooks:
            hook()
        execute_message_call(self, address)
        for hook in self._stop_sym_trans_hooks:
            hook()