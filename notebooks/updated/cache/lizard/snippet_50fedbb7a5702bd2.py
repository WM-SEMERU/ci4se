def get_raw_default_config_and_read_file_list():
    global _CONFIG, _READ_DEFAULT_FILES
    if _CONFIG is not None:
        return _CONFIG, _READ_DEFAULT_FILES
    with _CONFIG_LOCK:
        if _CONFIG is not None:
            return _CONFIG, _READ_DEFAULT_FILES
        try:
            from ConfigParser import SafeConfigParser
        except ImportError:
            from configparser import ConfigParser as SafeConfigParser
        cfg = SafeConfigParser()
        read_files = cfg.read(get_default_config_filename())
        _CONFIG, _READ_DEFAULT_FILES = cfg, read_files
        return _CONFIG, _READ_DEFAULT_FILES