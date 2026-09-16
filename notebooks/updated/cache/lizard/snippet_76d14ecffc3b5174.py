def lines_stats(dir_path, file_filter):
    n_files = 0
    n_lines = 0
    for p in Path(dir_path).select_file(file_filter):
        n_files += 1
        n_lines += count_lines(p.abspath)
    return n_files, n_lines