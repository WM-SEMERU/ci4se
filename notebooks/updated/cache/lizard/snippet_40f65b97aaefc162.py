def mongodump(mongo_user, mongo_password, mongo_dump_directory_path,
    database=None, silent=False):
    if path.exists(mongo_dump_directory_path):
        rmtree(mongo_dump_directory_path)
    if silent:
        dump_command = 'mongodump --quiet -u %s -p %s -o %s' % (mongo_user,
            mongo_password, mongo_dump_directory_path)
    else:
        dump_command = 'mongodump -u %s -p %s -o %s' % (mongo_user,
            mongo_password, mongo_dump_directory_path)
    if database:
        dump_command += ' --db %s' % database
    call(dump_command, silent=silent)