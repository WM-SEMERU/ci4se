def _run_polysquare_style_linter(matched_filenames, cache_dir, show_lint_files
    ):
    from polysquarelinter import linter as lint
    from prospector.message import Message, Location
    return_dict = dict()

    def _custom_reporter(error, file_path):
        key = _Key(file_path, error[1].line, error[0])
        loc = Location(file_path, None, None, error[1].line, 0)
        return_dict[key] = Message('polysquare-generic-file-linter', error[
            0], loc, error[1].description)
    for filename in matched_filenames:
        _debug_linter_status('style-linter', filename, show_lint_files)
    lint._report_lint_error = _custom_reporter
    lint.main(['--spellcheck-cache=' + os.path.join(cache_dir, 'spelling'),
        '--stamp-file-path=' + os.path.join(cache_dir, 'jobstamps',
        'polysquarelinter'), '--log-technical-terms-to=' + os.path.join(
        cache_dir, 'technical-terms')] + matched_filenames + [
        '--block-regexps'] + _BLOCK_REGEXPS)
    return return_dict