def compile_link_import_strings(codes, build_dir=None, **kwargs):
    build_dir = build_dir or tempfile.mkdtemp()
    if not os.path.isdir(build_dir):
        raise OSError('Non-existent directory: ', build_dir)
    source_files = []
    if kwargs.get('logger', False) is True:
        import logging
        logging.basicConfig(level=logging.DEBUG)
        kwargs['logger'] = logging.getLogger()
    only_update = kwargs.get('only_update', True)
    for name, code_ in codes:
        dest = os.path.join(build_dir, name)
        differs = True
        md5_in_mem = md5_of_string(code_.encode('utf-8')).hexdigest()
        if only_update and os.path.exists(dest):
            if os.path.exists(dest + '.md5'):
                md5_on_disk = open(dest + '.md5', 'rt').read()
            else:
                md5_on_disk = md5_of_file(dest).hexdigest()
            differs = md5_on_disk != md5_in_mem
        if not only_update or differs:
            with open(dest, 'wt') as fh:
                fh.write(code_)
                open(dest + '.md5', 'wt').write(md5_in_mem)
        source_files.append(dest)
    return compile_link_import_py_ext(source_files, build_dir=build_dir, **
        kwargs)