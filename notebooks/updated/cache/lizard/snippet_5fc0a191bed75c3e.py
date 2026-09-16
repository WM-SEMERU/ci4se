def cprint(text='', color=None, on_color=None, attrs=None, **kwargs):
    columns, lines = shutil.get_terminal_size()
    if columns == 0:
        columns = 80
    termcolor.cprint(textwrap.fill(text, columns, drop_whitespace=False),
        color=color, on_color=on_color, attrs=attrs, **kwargs)