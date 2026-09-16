def _link_bam_file(in_file, new_dir, data):
    new_dir = utils.safe_makedir(new_dir)
    out_file = os.path.join(new_dir, os.path.basename(in_file))
    if not utils.file_exists(out_file):
        out_file = os.path.join(new_dir, '%s-prealign.bam' % dd.
            get_sample_name(data))
    if data.get('cwl_keys'):
        if utils.file_exists(in_file + '.bai'):
            out_file = in_file
        else:
            utils.copy_plus(in_file, out_file)
    else:
        utils.symlink_plus(in_file, out_file)
    return out_file