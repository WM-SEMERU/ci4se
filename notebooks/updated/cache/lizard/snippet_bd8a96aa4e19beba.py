def summary(self, stream):
    if len(self.node_descs) == 1:
        self.sep(stream, '-', 'coverage: %s' % ''.join(self.node_descs))
    else:
        self.sep(stream, '-', 'coverage')
        for node_desc in sorted(self.node_descs):
            self.sep(stream, ' ', '%s' % node_desc)
    if 'term' in self.cov_report or 'term-missing' in self.cov_report:
        show_missing = 'term-missing' in self.cov_report
        self.cov.report(show_missing=show_missing, ignore_errors=True, file
            =stream)
    if 'annotate' in self.cov_report:
        self.cov.annotate(ignore_errors=True)
        stream.write('Coverage annotated source written next to source\n')
    if 'html' in self.cov_report:
        self.cov.html_report(ignore_errors=True)
        stream.write('Coverage HTML written to dir %s\n' % self.cov.config.
            html_dir)
    if 'xml' in self.cov_report:
        self.cov.xml_report(ignore_errors=True)
        stream.write('Coverage XML written to file %s\n' % self.cov.config.
            xml_output)
    if self.failed_slaves:
        self.sep(stream, '-', 'coverage: failed slaves')
        stream.write(
            """The following slaves failed to return coverage data, ensure that pytest-cov is installed on these slaves.
"""
            )
        for node in self.failed_slaves:
            stream.write('%s\n' % node.gateway.id)