def extract_files(ubifs, out_path, perms=False):
    try:
        inodes = {}
        bad_blocks = []
        walk.index(ubifs, ubifs.master_node.root_lnum, ubifs.master_node.
            root_offs, inodes, bad_blocks)
        if len(inodes) < 2:
            raise Exception('No inodes found')
        for dent in inodes[1]['dent']:
            extract_dents(ubifs, inodes, dent, out_path, perms)
        if len(bad_blocks):
            error(extract_files, 'Warning', 
                'Data may be missing or corrupted, bad blocks, LEB [%s]' %
                ','.join(map(str, bad_blocks)))
    except Exception as e:
        error(extract_files, 'Error', '%s' % e)