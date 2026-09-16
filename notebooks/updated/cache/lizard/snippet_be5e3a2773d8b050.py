def resolve_format(format, path):
    if format is None:
        if re.match('.+\\.(yml|yaml)$', path):
            return 'yaml'
        elif re.match('.+\\.tsv$', path):
            return 'tsv'
    else:
        return format.lower()