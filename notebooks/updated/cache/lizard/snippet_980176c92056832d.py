def entry_verifier(entries, regex, delimiter):
    cregex = re.compile(regex)
    python_version = int(sys.version.split('.')[0])
    decoder = 'unicode-escape' if python_version == 3 else 'string-escape'
    dedelimiter = codecs.decode(delimiter, decoder)
    for entry in entries:
        match = re.match(cregex, entry)
        if not match:
            split_regex = regex.split(delimiter)
            split_entry = entry.split(dedelimiter)
            part = 0
            for regex_segment, entry_segment in zip(split_regex, split_entry):
                if not regex_segment[0] == '^':
                    regex_segment = '^' + regex_segment
                if not regex_segment[-1] == '$':
                    regex_segment += '$'
                if not re.match(regex_segment, entry_segment):
                    raise FormatError(template=regex_segment, subject=
                        entry_segment, part=part)
                part += 1