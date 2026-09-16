def convert_libraries_in_path(config_path, lib_path, target_path=None):
    for lib in os.listdir(lib_path):
        if os.path.isdir(os.path.join(lib_path, lib)) and not '.' == lib[0]:
            if os.path.exists(os.path.join(os.path.join(lib_path, lib),
                'statemachine.yaml')) or os.path.exists(os.path.join(os.
                path.join(lib_path, lib), 'statemachine.json')):
                if not target_path:
                    convert(config_path, os.path.join(lib_path, lib))
                else:
                    convert(config_path, os.path.join(lib_path, lib), os.
                        path.join(target_path, lib))
            elif not target_path:
                convert_libraries_in_path(config_path, os.path.join(
                    lib_path, lib))
            else:
                convert_libraries_in_path(config_path, os.path.join(
                    lib_path, lib), os.path.join(target_path, lib))
        elif os.path.isdir(os.path.join(lib_path, lib)) and '.' == lib[0]:
            logger.debug(
                'lib_root_path/lib_path .*-folder are ignored if within lib_path, e.g. -> {0} -> full path is {1}'
                .format(lib, os.path.join(lib_path, lib)))