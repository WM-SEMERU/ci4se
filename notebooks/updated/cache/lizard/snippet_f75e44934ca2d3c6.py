def DownloadReportToFile(self, report_job_id, export_format, outfile,
    include_report_properties=False, include_totals_row=None,
    use_gzip_compression=True):
    service = self._GetReportService()
    if include_totals_row is None:
        include_totals_row = True if export_format != 'CSV_DUMP' else False
    opts = {'exportFormat': export_format, 'includeReportProperties':
        include_report_properties, 'includeTotalsRow': include_totals_row,
        'useGzipCompression': use_gzip_compression}
    report_url = service.getReportDownloadUrlWithOptions(report_job_id, opts)
    _data_downloader_logger.info('Request Summary: Report job ID: %s, %s',
        report_job_id, opts)
    response = self.url_opener.open(report_url)
    _data_downloader_logger.debug(
        'Incoming response: %s %s REDACTED REPORT DATA', response.code,
        response.msg)
    while True:
        chunk = response.read(_CHUNK_SIZE)
        if not chunk:
            break
        outfile.write(chunk)