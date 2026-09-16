def uncompressed_size(filename):
    quoted_filename = shlex.quote(filename)
    if str(filename).lower().endswith('.xz'):
        output = execute_command('xz --list "{}"'.format(quoted_filename))
        compressed, uncompressed = regexp_sizes.findall(output)
        value, unit = uncompressed.split()
        value = float(value.replace(',', ''))
        return int(value * MULTIPLIERS[unit])
    elif str(filename).lower().endswith('.gz'):
        output = execute_command('gzip --list "{}"'.format(quoted_filename))
        lines = [line.split() for line in output.splitlines()]
        header, data = lines[0], lines[1]
        gzip_data = dict(zip(header, data))
        return int(gzip_data['uncompressed'])
    else:
        raise ValueError('Unrecognized file type for "{}".'.format(filename))