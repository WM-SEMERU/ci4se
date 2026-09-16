def _read_and_convert(self, filepath, all_values):
    d = get_dict_from_ini(filepath)
    result = {}
    for key, func in self.ini_converter_dict.items():
        if not all_values and key not in d:
            continue
        try:
            value = d[key]
        except KeyError as err:
            traceback.print_exc()
            print('_' * 79)
            print('ERROR: %r is missing in your config!' % err)
            print("Debug '%s':" % filepath)
            try:
                print(pprint.pformat(d))
            except KeyError:
                pass
            print('\n')
            if click.confirm('Open the editor?'):
                self.open_editor()
            sys.exit(-1)
        if func:
            try:
                value = func(value)
            except (KeyError, ValueError) as err:
                edit_ini(self.ini_filepath)
                raise Exception("%s - .ini file: '%s'" % (err, self.
                    ini_filepath))
        result[key] = value
    return result