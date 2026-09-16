def get_sort_cmd(tmp_dir=None):
    has_versionsort = subprocess.check_output(
        'sort --help | grep version-sort; exit 0', shell=True).strip()
    if has_versionsort:
        cmd = 'sort -V'
    else:
        cmd = 'sort'
    if tmp_dir and os.path.exists(tmp_dir) and os.path.isdir(tmp_dir):
        cmd += ' -T %s' % tmp_dir
    return cmd