def thumbnail_preview(src_path):
    try:
        assert exists(src_path)
        width = '1980'
        dest_dir = mkdtemp(prefix='pyglass')
        cmd = [QLMANAGE, '-t', '-s', width, src_path, '-o', dest_dir]
        assert check_call(cmd) == 0
        src_filename = basename(src_path)
        dest_list = glob(join(dest_dir, '%s.png' % src_filename))
        assert dest_list
        dest_path = dest_list[0]
        assert exists(dest_path)
        return dest_path
    except:
        return None