def run_stop_backup(cls):

    def handler(popen):
        assert popen.returncode != 0
        raise UserException('Could not stop hot backup')
    return cls._dict_transform(psql_csv_run(
        "SELECT file_name,   lpad(file_offset::text, 8, '0') AS file_offset FROM pg_{0}file_name_offset(  pg_stop_backup())"
        .format(cls._wal_name()), error_handler=handler))