def comment_magic(source, language='python', global_escape_flag=True):
    parser = StringParser(language)
    next_is_magic = False
    for pos, line in enumerate(source):
        if not parser.is_quoted() and (next_is_magic or is_magic(line,
            language, global_escape_flag)):
            source[pos] = _COMMENT[language] + ' ' + line
            next_is_magic = (language == 'python' and _LINE_CONTINUATION_RE
                .match(line))
        parser.read_line(line)
    return source