def run_validator(pattern):
    start = ''
    if isinstance(pattern, six.string_types):
        start = pattern[:2]
        pattern = InputStream(pattern)
    if not start:
        start = pattern.readline()[:2]
        pattern.seek(0)
    parseErrListener = STIXPatternErrorListener()
    lexer = STIXPatternLexer(pattern)
    lexer.removeErrorListeners()
    stream = CommonTokenStream(lexer)
    parser = STIXPatternParser(stream)
    parser.buildParseTrees = False
    parser.removeErrorListeners()
    parser.addErrorListener(parseErrListener)
    for i, lit_name in enumerate(parser.literalNames):
        if lit_name == '<INVALID>':
            parser.literalNames[i] = parser.symbolicNames[i]
    parser.pattern()
    if not (start[0] == '[' or start == '(['):
        parseErrListener.err_strings[0
            ] = 'FAIL: Error found at line 1:0. input is missing square brackets'
    return parseErrListener.err_strings