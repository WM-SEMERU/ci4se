def parse_changelog(changes_path):
    if not exists(changes_path):
        raise Error("changelog file '%s' not found" % changes_path)
    content = codecs.open(changes_path, 'r', 'utf-8').read()
    parser = re.compile(
        '^##\\s*(?P<verline>[^\\n]*?)\\s*$(?P<body>.*?)(?=^##|\\Z)', re.M |
        re.S)
    sections = parser.findall(content)
    if not sections:
        template = '## 1.0.0 (not yet released)\n\n(nothing yet)\n'
        raise Error(
            "changelog '%s' must have at least one section, suggestion:\n\n%s"
             % (changes_path, _indent(template)))
    first_section_verline = sections[0][0]
    nyr = ' (not yet released)'
    items = []
    for i, section in enumerate(sections):
        item = {'verline': section[0], 'body': section[1]}
        if i == 0:
            verline = section[0]
            if verline.endswith(nyr):
                verline = verline[0:-len(nyr)]
            version = verline.split()[-1]
            try:
                int(version[0])
            except ValueError:
                msg = ''
                if version.endswith(')'):
                    msg = (
                        ' (cutarelease is picky about the trailing %r on the top version line. Perhaps you misspelled that?)'
                         % nyr)
                raise Error(
                    "changelog '%s' top section version '%s' is invalid: first char isn't a number%s"
                     % (changes_path, version, msg))
            item['version'] = version
        items.append(item)
    return content, items, nyr