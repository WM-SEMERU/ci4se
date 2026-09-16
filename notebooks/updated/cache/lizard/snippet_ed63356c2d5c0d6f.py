def add_report(self, report, ignore_errors=False):
    if not isinstance(report, SignedListReport):
        if ignore_errors:
            return
        raise ArgumentError(
            'You can only add SignedListReports to a UTCAssigner', report=
            report)
    for reading in report.visible_readings:
        self.add_reading(reading)
    self.add_point(report.report_id, report.sent_timestamp, report.
        received_time)