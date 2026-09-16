def load_data(cr, module_name, filename, idref=None, mode='init'):
    if idref is None:
        idref = {}
    logger.info('%s: loading %s' % (module_name, filename))
    _, ext = os.path.splitext(filename)
    pathname = os.path.join(module_name, filename)
    fp = tools.file_open(pathname)
    try:
        if ext == '.csv':
            noupdate = True
            tools.convert_csv_import(cr, module_name, pathname, fp.read(),
                idref, mode, noupdate)
        elif ext == '.yml':
            yaml_import(cr, module_name, fp, None, idref=idref, mode=mode)
        elif mode == 'init_no_create':
            for fp2 in _get_existing_records(cr, fp, module_name):
                tools.convert_xml_import(cr, module_name, fp2, idref, mode=
                    'init')
        else:
            tools.convert_xml_import(cr, module_name, fp, idref, mode=mode)
    finally:
        fp.close()