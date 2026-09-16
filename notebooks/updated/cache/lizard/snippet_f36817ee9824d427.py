def _format_files(cls, files, kind):
    lines = []
    if files:
        lines.append('The following {kind} are contained in this DAP:'.
            format(kind=kind.title()))
        for f in files:
            lines.append('* ' + strip_prefix(f, kind).replace(os.path.sep,
                ' ').strip())
        return lines
    else:
        return ['No {kind} are contained in this DAP'.format(kind=kind.title())
            ]