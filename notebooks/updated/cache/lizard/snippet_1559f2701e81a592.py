def bandwidth(self):
    self._bandwidth = self.lib.iperf_get_test_rate(self._test)
    return self._bandwidth