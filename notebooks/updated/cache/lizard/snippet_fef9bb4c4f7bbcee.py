def get_logs(self, stdout=True, stderr=True, timestamps=False, tail='all',
    since=None):
    return self.inner().logs(stdout=stdout, stderr=stderr, timestamps=
        timestamps, tail=tail, since=since)