def compat_stat(path):
    stat = os.stat(path)
    info = get_file_info(path)
    return nt.stat_result((stat.st_mode,) + (info.file_index, info.
        volume_serial_number, info.number_of_links) + stat[4:])