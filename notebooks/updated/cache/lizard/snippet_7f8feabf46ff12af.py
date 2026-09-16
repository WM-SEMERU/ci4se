def _record_revisit(self, payload_offset: int):
    fields = self._response_record.fields
    ref_record_id = self._url_table.get_revisit_id(fields['WARC-Target-URI'
        ], fields.get('WARC-Payload-Digest', '').upper().replace('SHA1:', ''))
    if ref_record_id:
        try:
            self._response_record.block_file.truncate(payload_offset)
        except TypeError:
            self._response_record.block_file.seek(0)
            data = self._response_record.block_file.read(payload_offset)
            self._response_record.block_file.truncate()
            self._response_record.block_file.seek(0)
            self._response_record.block_file.write(data)
        self._recorder.set_length_and_maybe_checksums(self._response_record)
        fields[WARCRecord.WARC_TYPE] = WARCRecord.REVISIT
        fields['WARC-Refers-To'] = ref_record_id
        fields['WARC-Profile'] = WARCRecord.SAME_PAYLOAD_DIGEST_URI
        fields['WARC-Truncated'] = 'length'