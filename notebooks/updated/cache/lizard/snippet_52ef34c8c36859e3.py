def make_tmp_dir(prefix):
    now = datetime.now().isoformat()
    f_uuid = uuid.uuid4().hex
    out_dir = '{out}/{p}-{now}-{uuid}'.format(out=_output_dir, p=prefix,
        now=now, uuid=f_uuid)
    if not _dry_run:
        os.makedirs(out_dir)
    log.msg_debug('Output directory: {out_dir}'.format(out_dir=_output_dir))
    return out_dir