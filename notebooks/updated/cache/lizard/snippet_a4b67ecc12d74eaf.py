def run(self, call, num_alts):
    for key, value in call.data.items():
        self._check_count(call, key, value, num_alts)