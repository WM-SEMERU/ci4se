def _report_spelling_error(error, file_path):
    line = error.line_offset + 1
    code = 'file/spelling_error'
    description = _SPELLCHECK_MESSAGES[error.error_type].format(error.word)
    if error.suggestions is not None:
        description = description + ', perhaps you meant: ' + ', '.join(error
            .suggestions)
    sys.stdout.write('{0}:{1} [{2}] {3}\n'.format(file_path, line, code,
        description))