def _cnvkit_metrics(cnns, target_bed, antitarget_bed, cov_interval, items):
    if cov_interval == 'genome':
        return cnns
    target_cnn = [x['file'] for x in cnns if x['cnntype'] == 'target'][0]
    background_file = '%s-flatbackground.cnn' % utils.splitext_plus(target_cnn
        )[0]
    background_file = cnvkit_background([], background_file, items,
        target_bed, antitarget_bed)
    cnr_file, data = _cnvkit_fix_base(cnns, background_file, items,
        '-flatbackground')
    cns_file = _cnvkit_segment(cnr_file, cov_interval, data)
    metrics_file = '%s-metrics.txt' % utils.splitext_plus(target_cnn)[0]
    if not utils.file_exists(metrics_file):
        with file_transaction(data, metrics_file) as tx_metrics_file:
            cmd = [_get_cmd(), 'metrics', '-o', tx_metrics_file, '-s',
                cns_file, '--', cnr_file]
            do.run(_prep_cmd(cmd, tx_metrics_file), 'CNVkit metrics')
    metrics = _read_metrics_file(metrics_file)
    out = []
    for cnn in cnns:
        cnn['metrics'] = metrics
        out.append(cnn)
    return out