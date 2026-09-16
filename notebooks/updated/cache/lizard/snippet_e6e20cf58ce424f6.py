def show(all_keys):
    if not config_file_exists():
        echo_info('No config file found! Please try `ddev config restore`.')
    elif all_keys:
        echo_info(read_config_file().rstrip())
    else:
        echo_info(read_config_file_scrubbed().rstrip())