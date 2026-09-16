def init():
    global ASMS
    global ASMCOUNT
    global AT_END
    global FLAG_end_emitted
    global FLAG_use_function_exit
    __common.init()
    ASMS = {}
    ASMCOUNT = 0
    AT_END = []
    FLAG_use_function_exit = False
    FLAG_end_emitted = False
    OPTIONS.add_option('org', int, 32768)
    OPTIONS.add_option('heap_size', int, 4768)
    OPTIONS.add_option('heap_start_label', str, 'ZXBASIC_MEM_HEAP')
    OPTIONS.add_option('heap_size_label', str, 'ZXBASIC_HEAP_SIZE')
    OPTIONS.add_option('headerless', bool, False)