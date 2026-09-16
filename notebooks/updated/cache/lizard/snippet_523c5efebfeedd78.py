def create_file(self, filename):
    self.response.write('Creating file %s\n' % filename)
    write_retry_params = gcs.RetryParams(backoff_factor=1.1)
    gcs_file = gcs.open(filename, 'w', content_type='text/plain', options={
        'x-goog-meta-foo': 'foo', 'x-goog-meta-bar': 'bar'}, retry_params=
        write_retry_params)
    gcs_file.write('abcde\n')
    gcs_file.write('f' * 1024 * 4 + '\n')
    gcs_file.close()
    self.tmp_filenames_to_clean_up.append(filename)