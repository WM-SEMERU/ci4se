def dump_json_file(json_data, pwd_dir_path, dump_file_name):


    class PythonObjectEncoder(json.JSONEncoder):

        def default(self, obj):
            try:
                return super().default(self, obj)
            except TypeError:
                return str(obj)
    logs_dir_path = os.path.join(pwd_dir_path, 'logs')
    if not os.path.isdir(logs_dir_path):
        os.makedirs(logs_dir_path)
    dump_file_path = os.path.join(logs_dir_path, dump_file_name)
    try:
        with io.open(dump_file_path, 'w', encoding='utf-8') as outfile:
            if is_py2:
                outfile.write(unicode(json.dumps(json_data, indent=4,
                    separators=(',', ':'), ensure_ascii=False, cls=
                    PythonObjectEncoder)))
            else:
                json.dump(json_data, outfile, indent=4, separators=(',',
                    ':'), ensure_ascii=False, cls=PythonObjectEncoder)
        msg = 'dump file: {}'.format(dump_file_path)
        logger.color_print(msg, 'BLUE')
    except TypeError as ex:
        msg = 'Failed to dump json file: {}\nReason: {}'.format(dump_file_path,
            ex)
        logger.color_print(msg, 'RED')