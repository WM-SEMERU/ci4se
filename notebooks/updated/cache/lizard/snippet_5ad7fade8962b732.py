def _rewrite_paths_in_file(config_file, paths_to_replace):
    lines = []
    import shutil
    shutil.copyfile(config_file, str(config_file + '_original'))
    with open(config_file) as infile:
        for line in infile:
            for old_path in paths_to_replace:
                if old_path in line:
                    new_path = os.path.split(old_path)[-1]
                    line = line.replace(old_path, new_path)
                    logger.debug('Changed path {0} ---> {1} in file {2}'.
                        format(old_path, new_path, config_file))
            lines.append(line)
    with open(config_file, 'w') as outfile:
        for line in lines:
            outfile.write(line)