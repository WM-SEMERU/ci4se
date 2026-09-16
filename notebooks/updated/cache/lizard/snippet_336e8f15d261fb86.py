def close(self):
    if self._log_temp_file:
        self._log_handler.flush()
        logger = logging.getLogger()
        logger.removeHandler(self._log_handler)
        self._log_handler.stream.close()
        log_record = WARCRecord()
        log_record.block_file = gzip.GzipFile(filename=self._log_temp_file.name
            )
        log_record.set_common_fields('resource', 'text/plain')
        log_record.fields['WARC-Target-URI'] = 'urn:X-wpull:log'
        if self._params.max_size is not None:
            if self._params.move_to is not None:
                self._move_file_to_dest_dir(self._warc_filename)
            self._start_new_warc_file(meta=True)
        self.set_length_and_maybe_checksums(log_record)
        self.write_record(log_record)
        log_record.block_file.close()
        try:
            os.remove(self._log_temp_file.name)
        except OSError:
            _logger.exception('Could not close log temp file.')
        self._log_temp_file = None
        self._log_handler.close()
        self._log_handler = None
        if self._params.move_to is not None:
            self._move_file_to_dest_dir(self._warc_filename)
    if self._cdx_filename and self._params.move_to is not None:
        self._move_file_to_dest_dir(self._cdx_filename)