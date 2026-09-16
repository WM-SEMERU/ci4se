def _copy_or_render_source(ext, f, output_dir, render_callback, skip_copy=False
    ):
    dirname = os.path.dirname(f)
    filename = os.path.basename(f)
    for pattern, target, subsd in ext.template_regexps:
        if re.match(pattern, filename):
            tgt = os.path.join(dirname, re.sub(pattern, target, filename))
            rw = MetaReaderWriter('.metadata_subsd')
            try:
                prev_subsd = rw.get_from_metadata_file(output_dir, f)
            except (FileNotFoundError, KeyError):
                prev_subsd = None
            render_callback(get_abspath(f), os.path.join(output_dir, tgt),
                subsd, only_update=ext.only_update, prev_subsd=prev_subsd,
                create_dest_dirs=True, logger=ext.logger)
            rw.save_to_metadata_file(output_dir, f, subsd)
            return tgt
    else:
        if not skip_copy:
            copy(f, os.path.join(output_dir, os.path.dirname(f)),
                only_update=ext.only_update, dest_is_dir=True,
                create_dest_dirs=True, logger=ext.logger)
        return f