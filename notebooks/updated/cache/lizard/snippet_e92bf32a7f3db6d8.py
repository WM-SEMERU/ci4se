def _PrintExtractionStatusUpdateLinear(self, processing_status):
    for worker_status in processing_status.workers_status:
        status_line = (
            """{0:s} (PID: {1:d}) - events produced: {2:d} - file: {3:s} - running: {4!s}
"""
            .format(worker_status.identifier, worker_status.pid,
            worker_status.number_of_produced_events, worker_status.
            display_name, worker_status.status not in definitions.
            ERROR_STATUS_INDICATORS))
        self._output_writer.Write(status_line)