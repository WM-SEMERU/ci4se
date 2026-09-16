def create(self, name, data):
    return self._update('/job-binary-internals/%s' % urlparse.quote(name.
        encode('utf-8')), data, 'job_binary_internal', dump_json=False)