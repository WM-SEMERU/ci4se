def load_ipython_extension(ip):
    ip.register_magics(FortranMagics)
    patch = (
        "IPython.config.cell_magic_highlight['magic_fortran'] = {'reg':[/^%%fortran/]};"
        )
    js = display.Javascript(data=patch, lib=[
        'https://raw.github.com/marijnh/CodeMirror/master/mode/fortran/fortran.js'
        ])
    display.display_javascript(js)