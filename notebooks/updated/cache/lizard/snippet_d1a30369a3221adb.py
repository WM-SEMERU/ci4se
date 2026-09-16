def init():
    global OUTPUT
    global INCLUDED
    global CURRENT_DIR
    global ENABLED
    global INCLUDEPATH
    global IFDEFS
    global ID_TABLE
    global CURRENT_FILE
    global_.FILENAME = '(stdin)'
    OUTPUT = ''
    INCLUDED = {}
    CURRENT_DIR = ''
    pwd = get_include_path()
    INCLUDEPATH = [os.path.join(pwd, 'library'), os.path.join(pwd,
        'library-asm')]
    ENABLED = True
    IFDEFS = []
    global_.has_errors = 0
    global_.error_msg_cache.clear()
    parser.defaulted_states = {}
    ID_TABLE = DefinesTable()
    del CURRENT_FILE[:]