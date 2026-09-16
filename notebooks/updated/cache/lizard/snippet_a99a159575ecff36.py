def wait_for_logs_matching(self, matcher, timeout=10, encoding='utf-8', **
    logs_kwargs):
    wait_for_logs_matching(self.inner(), matcher, timeout=timeout, encoding
        =encoding, **logs_kwargs)