def parse_file(self, cu, analysis):
    if hasattr(analysis, 'parser'):
        filename = cu.file_locator.relative_filename(cu.filename)
        source_lines = analysis.parser.lines
        with cu.source_file() as source_file:
            source = source_file.read()
        try:
            if sys.version_info < (3, 0):
                encoding = source_encoding(source)
                if encoding != 'utf-8':
                    source = source.decode(encoding).encode('utf-8')
        except UnicodeDecodeError:
            log.warning(
                'Source file %s can not be properly decoded, skipping. Please check if encoding declaration is ok'
                , os.path.basename(cu.filename))
            return
    else:
        if hasattr(cu, 'relative_filename'):
            filename = cu.relative_filename()
        else:
            filename = analysis.coverage.file_locator.relative_filename(cu.
                filename)
        token_lines = analysis.file_reporter.source_token_lines()
        source_lines = list(enumerate(token_lines))
        source = analysis.file_reporter.source()
    coverage_lines = [self.get_hits(i, analysis) for i in range(1, len(
        source_lines) + 1)]
    posix_filename = filename.replace(os.path.sep, '/')
    results = {'name': posix_filename, 'source': source, 'coverage':
        coverage_lines}
    branches = self.get_arcs(analysis)
    if branches:
        results['branches'] = branches
    self.source_files.append(results)