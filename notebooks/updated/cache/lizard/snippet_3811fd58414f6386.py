def autofix_codeblock(codeblock, max_line_len=80, aggressive=False,
    very_aggressive=False, experimental=False):
    r
    import autopep8
    arglist = ['--max-line-length', '80']
    if aggressive:
        arglist.extend(['-a'])
    if very_aggressive:
        arglist.extend(['-a', '-a'])
    if experimental:
        arglist.extend(['--experimental'])
    arglist.extend([''])
    autopep8_options = autopep8.parse_args(arglist)
    fixed_codeblock = autopep8.fix_code(codeblock, options=autopep8_options)
    return fixed_codeblock