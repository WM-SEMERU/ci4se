def whitespace_before_comment(logical_line, tokens):
    r
    prev_end = 0, 0
    for token_type, text, start, end, line in tokens:
        if token_type == tokenize.COMMENT:
            inline_comment = line[:start[1]].strip()
            if inline_comment:
                if prev_end[0] == start[0] and start[1] < prev_end[1] + 2:
                    yield prev_end, 'E261 at least two spaces before inline comment'
            symbol, sp, comment = text.partition(' ')
            bad_prefix = symbol not in '#:' and (symbol.lstrip('#')[:1] or '#')
            if inline_comment:
                if bad_prefix or comment[:1] in WHITESPACE:
                    yield start, "E262 inline comment should start with '# '"
            elif bad_prefix and (bad_prefix != '!' or start[0] > 1):
                if bad_prefix != '#':
                    yield start, "E265 block comment should start with '# '"
                elif comment:
                    yield start, "E266 too many leading '#' for block comment"
        elif token_type != tokenize.NL:
            prev_end = end