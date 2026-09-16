def scan_ipaddr(ipaddr, line, project, split_path, apikey):
    logger.info('Found what I believe is an IP Address: %s', line.strip())
    logger.info('File %s. Parsed IP Address: %s', split_path, ipaddr)
    with open(reports_dir + 'ips-' + project + '.log', 'a') as gate_report:
        gate_report.write(
            'File {} contains what I believe is an IP Address: {}\n'.format
            (split_path, ipaddr))
    v_api = virus_total.VirusTotal()
    scan_ip = v_api.send_ip(ipaddr, apikey)
    response_code = scan_ip['response_code']
    verbose_msg = scan_ip['verbose_msg']
    urls = scan_ip['detected_urls']
    with open(reports_dir + 'ips-' + project + '.log', 'a') as gate_report:
        if urls:
            logger.error(
                '%s has been known to resolve to the following malicious urls:'
                , ipaddr)
            gate_report.write(
                '{} has been known to resolve to the following malicious urls:\n'
                .format(ipaddr))
            for url in urls:
                logger.info('%s on date: %s', url['url'], url['scan_date'])
                gate_report.write('{} on {}\n'.format(url['url'], url[
                    'scan_date']))
                sleep(0.2)
        else:
            logger.info('No malicious DNS history found for: %s', ipaddr)
            gate_report.write('No malicious DNS history found for: {}\n'.
                format(ipaddr))