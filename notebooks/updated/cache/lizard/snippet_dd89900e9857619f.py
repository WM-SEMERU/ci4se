def filter_(input_, filename='<internal>', state='INITIAL'):
    global CURRENT_DIR
    prev_dir = CURRENT_DIR
    CURRENT_FILE.append(filename)
    CURRENT_DIR = os.path.dirname(CURRENT_FILE[-1])
    LEXER.input(input_, filename)
    LEXER.lex.begin(state)
    parser.parse(lexer=LEXER, debug=OPTIONS.Debug.value > 2)
    CURRENT_FILE.pop()
    CURRENT_DIR = prev_dir