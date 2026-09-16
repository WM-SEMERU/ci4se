def assert_dut_trace_not_contains(self, k, message):
    asserts.assertDutTraceDoesNotContain(k, message, bench=self.bench)