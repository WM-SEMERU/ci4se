def _PrintAnalysisStatusUpdateWindow(self, processing_status):
    if self._stdout_output_writer:
        self._ClearScreen()
    output_text = 'plaso - {0:s} version {1:s}\n\n'.format(self._tool_name,
        plaso.__version__)
    self._output_writer.Write(output_text)
    self._PrintAnalysisStatusHeader(processing_status)
    table_view = views.CLITabularTableView(column_names=['Identifier',
        'PID', 'Status', 'Memory', 'Events', 'Tags', 'Reports'],
        column_sizes=[23, 7, 15, 15, 15, 15, 0])
    self._AddsAnalysisProcessStatusTableRow(processing_status.
        foreman_status, table_view)
    for worker_status in processing_status.workers_status:
        self._AddsAnalysisProcessStatusTableRow(worker_status, table_view)
    table_view.Write(self._output_writer)
    self._output_writer.Write('\n')
    if processing_status.aborted:
        self._output_writer.Write(
            'Processing aborted - waiting for clean up.\n\n')
    if self._stdout_output_writer:
        sys.stdout.flush()