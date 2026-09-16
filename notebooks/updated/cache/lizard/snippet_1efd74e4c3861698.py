def dump_database(self):
    db_file = self.create_file_name(self.databases['source']['name'])
    self.print_message("Dumping postgres database '%s' to file '%s'" % (
        self.databases['source']['name'], db_file))
    self.export_pgpassword('source')
    args = ['pg_dump', '-Fc', '--no-acl', '--no-owner', '--dbname=%s' %
        self.databases['source']['name'], '--file=%s' % db_file]
    args.extend(self.databases['source']['args'])
    subprocess.check_call(args)
    return db_file