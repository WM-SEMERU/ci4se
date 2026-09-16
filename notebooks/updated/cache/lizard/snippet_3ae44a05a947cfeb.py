def negative_report(binary_report, sha256hash, project, patch_file):
    report_url = binary_report['permalink']
    scan_date = binary_report['scan_date']
    logger.info('File scan date for %s shows a clean status on: %s',
        patch_file, scan_date)
    logger.info('Full report avaliable here: %s', report_url)
    logger.info(
        'The following sha256 hash can be used in your %s.yaml file to suppress this scan:'
        , project)
    logger.info('%s', sha256hash)
    with open(reports_dir + 'binaries-' + project + '.log', 'a'
        ) as gate_report:
        gate_report.write('Non Whitelisted Binary: {}\n'.format(patch_file))
        gate_report.write('File scan date for {} shows a clean status on {}\n'
            .format(patch_file, scan_date))
        gate_report.write(
            """The following sha256 hash can be used in your {}.yaml file to suppress this scan:
"""
            .format(project))
        gate_report.write('{}\n'.format(sha256hash))