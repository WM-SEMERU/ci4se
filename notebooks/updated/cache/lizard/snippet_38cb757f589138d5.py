def copy_file_if_modified(src_path, dest_path):
    if os.path.isdir(dest_path):
        shutil.rmtree(dest_path)
    must_copy = False
    if not os.path.exists(dest_path):
        must_copy = True
    else:
        src_stat = os.stat(src_path)
        dest_stat = os.stat(dest_path)
        if src_stat[stat.ST_SIZE] != dest_stat[stat.ST_SIZE] or src_stat[
            stat.ST_MTIME] != dest_stat[stat.ST_MTIME]:
            must_copy = True
    if must_copy:
        shutil.copy2(src_path, dest_path)