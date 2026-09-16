def PDFTeXLaTeXFunction(target=None, source=None, env=None):
    basedir = os.path.split(str(source[0]))[0]
    abspath = os.path.abspath(basedir)
    if SCons.Tool.tex.is_LaTeX(source, env, abspath):
        result = PDFLaTeXAuxAction(target, source, env)
        if result != 0:
            SCons.Tool.tex.check_file_error_message(env['PDFLATEX'])
    else:
        result = PDFTeXAction(target, source, env)
        if result != 0:
            SCons.Tool.tex.check_file_error_message(env['PDFTEX'])
    return result