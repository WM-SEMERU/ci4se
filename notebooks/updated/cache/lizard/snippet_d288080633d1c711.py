def init_functions(connection):
    if settings.CFG['db']['create_functions']:
        print('Refreshing SQL functions...')
        for file in path.template_files('../sql/', exts=['.sql']):
            func = sa.DDL(path.template_str(file))
            LOG.info("Loading: '%s' into database", file)
            connection.execute(func)
            connection.commit()