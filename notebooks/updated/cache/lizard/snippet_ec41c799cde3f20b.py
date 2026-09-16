def parse_schedules(username, password, importer, progress, utc_start=None,
    utc_stop=None):
    file_obj = get_file_object(username, password, utc_start, utc_stop)
    process_file_object(file_obj, importer, progress)