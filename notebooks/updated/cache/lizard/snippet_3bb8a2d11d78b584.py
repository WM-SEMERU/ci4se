def PrintExtractionSummary(self, processing_status):
    if not processing_status:
        self._output_writer.Write(
            'WARNING: missing processing status information.\n')
    elif not processing_status.aborted:
        if processing_status.error_path_specs:
            self._output_writer.Write('Processing completed with errors.\n')
        else:
            self._output_writer.Write('Processing completed.\n')
        number_of_warnings = (processing_status.foreman_status.
            number_of_produced_warnings)
        if number_of_warnings:
            output_text = '\n'.join(['',
                'Number of warnings generated while extracting events: {0:d}.'
                .format(number_of_warnings), '',
                'Use pinfo to inspect warnings in more detail.', ''])
            self._output_writer.Write(output_text)
        if processing_status.error_path_specs:
            output_text = '\n'.join(['',
                'Path specifications that could not be processed:', ''])
            self._output_writer.Write(output_text)
            for path_spec in processing_status.error_path_specs:
                self._output_writer.Write(path_spec.comparable)
                self._output_writer.Write('\n')
    self._output_writer.Write('\n')