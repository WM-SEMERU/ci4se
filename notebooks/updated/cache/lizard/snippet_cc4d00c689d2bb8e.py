def tail(path, lines):
    path = os.path.expanduser(path)
    lines_found = []
    buffer_size = 4098
    if not os.path.isfile(path):
        raise SaltInvocationError('File not found: {0}'.format(path))
    if not __utils__['files.is_text'](path):
        raise SaltInvocationError('Cannot tail a binary file: {0}'.format(path)
            )
    try:
        lines = int(lines)
    except ValueError:
        raise SaltInvocationError("file.tail: 'lines' value must be an integer"
            )
    try:
        with salt.utils.fopen(path) as tail_fh:
            blk_cnt = 1
            size = os.stat(path).st_size
            if size > buffer_size:
                tail_fh.seek(-buffer_size * blk_cnt, os.SEEK_END)
            data = string.split(tail_fh.read(buffer_size), os.linesep)
            for i in range(lines):
                while len(data) == 1 and blk_cnt * buffer_size < size:
                    blk_cnt += 1
                    line = data[0]
                    try:
                        tail_fh.seek(-buffer_size * blk_cnt, os.SEEK_END)
                        data = string.split(tail_fh.read(buffer_size) +
                            line, os.linesep)
                    except IOError:
                        tail_fh.seek(0)
                        data = string.split(tail_fh.read(size - buffer_size *
                            (blk_cnt - 1)) + line, os.linesep)
                line = data[-1]
                data.pop()
                lines_found.append(line)
        return lines_found[-lines:]
    except (OSError, IOError):
        raise CommandExecutionError("Could not tail '{0}'".format(path))