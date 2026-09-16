def make_tex_table(inputlist, outputfilename, fmt=None, **kwargs):
    outputfilepath = FILEPATHSTR.format(root_dir=ROOT_DIR, os_sep=os.sep,
        os_extsep=os.extsep, name=outputfilename, folder=PURPOSE.get(
        'tables').get('folder', 'tables'), ext=PURPOSE.get('tables').get(
        'extension', 'tex'))
    table.make_tex_table(inputlist, open(outputfilepath, 'wb'), fmt=fmt,
        close=kwargs.get('close', True), **kwargs)