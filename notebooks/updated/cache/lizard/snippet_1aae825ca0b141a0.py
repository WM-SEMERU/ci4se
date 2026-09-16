def _rtg_add_summary_file(eval_files, base_dir, data):
    out_file = os.path.join(base_dir, 'validate-summary.csv')
    if not utils.file_uptodate(out_file, eval_files.get('tp', eval_files.
        get('fp', eval_files['fn']))):
        with file_transaction(data, out_file) as tx_out_file:
            with open(tx_out_file, 'w') as out_handle:
                writer = csv.writer(out_handle)
                writer.writerow(['sample', 'caller', 'vtype', 'metric',
                    'value'])
                base = _get_sample_and_caller(data)
                for metric in ['tp', 'fp', 'fn']:
                    for vtype, bcftools_types in [('SNPs', '--types snps'),
                        ('Indels', '--exclude-types snps')]:
                        in_file = eval_files.get(metric)
                        if in_file and os.path.exists(in_file):
                            cmd = (
                                'bcftools view {bcftools_types} {in_file} | grep -v ^# | wc -l'
                                )
                            count = int(subprocess.check_output(cmd.format(
                                **locals()), shell=True))
                        else:
                            count = 0
                        writer.writerow(base + [vtype, metric, count])
    eval_files['summary'] = out_file
    return eval_files