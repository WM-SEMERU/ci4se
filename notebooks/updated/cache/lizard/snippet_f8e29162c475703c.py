def check_shell_encoding(cls):
    is_in_utf8 = True
    is_out_utf8 = True
    if sys.stdin.encoding not in ['UTF-8', 'UTF8']:
        is_in_utf8 = False
    if sys.stdout.encoding not in ['UTF-8', 'UTF8']:
        is_out_utf8 = False
    if is_in_utf8 and is_out_utf8:
        gf.print_success('shell encoding OK')
    else:
        gf.print_warning('shell encoding WARNING')
        if not is_in_utf8:
            gf.print_warning(
                '  The default input encoding of your shell is not UTF-8')
        if not is_out_utf8:
            gf.print_warning(
                '  The default output encoding of your shell is not UTF-8')
        gf.print_info('  If you plan to use aeneas on the command line,')
        if gf.is_posix():
            gf.print_info(
                "  you might want to 'export PYTHONIOENCODING=UTF-8' in your shell"
                )
        else:
            gf.print_info(
                "  you might want to 'set PYTHONIOENCODING=UTF-8' in your shell"
                )
        return True
    return False