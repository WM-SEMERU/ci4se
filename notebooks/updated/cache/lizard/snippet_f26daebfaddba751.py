def convert_pg_command_version_to_number(command_version_string):
    match = re.search(' \\(PostgreSQL\\) ([0-9]+(?:\\.[0-9]+)+)',
        command_version_string)
    if not match:
        match = re.search(' \\(PostgreSQL\\) ([0-9]+)beta([0-9])',
            command_version_string)
        if not match:
            raise Error('Unrecognized PostgreSQL version string {!r}'.
                format(command_version_string))
    parts = match.group(1).split('.')
    if int(parts[0]) >= 10:
        if len(parts) == 1:
            return int(parts[0]) * 10000
        return int(parts[0]) * 10000 + int(parts[1])
    elif len(parts) == 2:
        parts.append('0')
    return int(parts[0]) * 10000 + int(parts[1]) * 100 + int(parts[2])