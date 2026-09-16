def read_packages(reqs_file):
    for line in stream_file_lines(reqs_file):
        line = line.strip()
        if not line.startswith(('#', '--hash')):
            match = DEP_PATTERN.match(line)
            if match:
                package, version, marker = match.groups()
                yield Package(package.lower(), version, marker)