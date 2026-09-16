def _summary_csv_by_researcher(summary_yaml, researcher, descrs, data):
    out_file = os.path.join(utils.safe_makedir(os.path.join(data['dirs'][
        'work'], 'researcher')), '%s-summary.tsv' % run_info.clean_name(
        researcher))
    metrics = ['Total_reads', 'Mapped_reads', 'Mapped_reads_pct',
        'Duplicates', 'Duplicates_pct']
    with open(summary_yaml) as in_handle:
        with open(out_file, 'w') as out_handle:
            writer = csv.writer(out_handle, dialect='excel-tab')
            writer.writerow(['Name'] + metrics)
            for sample in yaml.safe_load(in_handle)['samples']:
                if sample['description'] in descrs:
                    row = [sample['description']] + [utils.get_in(sample, (
                        'summary', 'metrics', x), '') for x in metrics]
                    writer.writerow(row)
    return out_file