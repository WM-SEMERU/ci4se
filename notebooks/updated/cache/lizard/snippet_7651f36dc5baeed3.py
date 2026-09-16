def pwarning(*args, **kwargs):
    if should_msg(kwargs.get('groups', ['warning'])):
        global colorama_init
        if not colorama_init:
            colorama_init = True
            colorama.init()
        args = indent_text(*args, **kwargs)
        sys.stderr.write(colorama.Fore.YELLOW)
        sys.stderr.write(''.join(args))
        sys.stderr.write(colorama.Fore.RESET)
        sys.stderr.write('\n')