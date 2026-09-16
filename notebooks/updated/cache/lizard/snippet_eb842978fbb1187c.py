def scan_ipaddr(ipaddr, apikey):
    logger.info('Query VirusTotal API for Public IP Found: %s', ipaddr)
    v_api = virus_total.VirusTotal()
    scan_ip = v_api.send_ip(ipaddr, apikey)
    response_code = scan_ip['response_code']
    verbose_msg = scan_ip['verbose_msg']
    urls = scan_ip['detected_urls']
    if urls:
        failure = True
        logger.error('%s has been known to resolve to malicious urls', ipaddr)
        for url in urls:
            logger.error('%s on date: %s', url['url'], url['scan_date'])
    else:
        logger.info('%s has no record of resolving to malicious urls', ipaddr)