def filter_osm_file():
    print_info('Filtering OSM file...')
    start_time = time.time()
    if check_osmfilter():
        params = config.osm_filter_params
        command = './osmfilter' if platform.system(
            ) == 'Linux' else 'osmfilter.exe'
        if platform.system() == 'Linux':
            filter_command = '%s "%s" %s | pv > "%s"' % (command, config.
                osm_map_filename, params, config.filtered_osm_filename)
        else:
            filter_command = '%s "%s" %s > "%s"' % (command, config.
                osm_map_filename, params, config.filtered_osm_filename)
        os.system(filter_command)
    else:
        print_info('Osmfilter not available. Exiting.')
        exit(1)
    print_info('Filtering finished. (%.2f secs)' % (time.time() - start_time))