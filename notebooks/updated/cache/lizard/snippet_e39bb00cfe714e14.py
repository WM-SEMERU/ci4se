def _add_warc_snapshot(self, filename, url):
    _logger.debug('Adding snapshot record.')
    extension = os.path.splitext(filename)[1]
    content_type = {'.pdf': 'application/pdf', '.html': 'text/html', '.png':
        'image/png', '.gif': 'image/gif'}[extension]
    record = WARCRecord()
    record.set_common_fields('resource', content_type)
    record.fields['WARC-Target-URI'] = 'urn:X-wpull:snapshot?url={0}'.format(
        wpull.url.percent_encode_query_value(url))
    if self._action_warc_record:
        record.fields['WARC-Concurrent-To'] = self._action_warc_record.fields[
            WARCRecord.WARC_RECORD_ID]
    with open(filename, 'rb') as in_file:
        record.block_file = in_file
        self._warc_recorder.set_length_and_maybe_checksums(record)
        self._warc_recorder.write_record(record)