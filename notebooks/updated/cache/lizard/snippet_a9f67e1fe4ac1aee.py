def request_file(link, outfile, force_rerun_flag=False):
    if force_rerun(flag=force_rerun_flag, outfile=outfile):
        req = requests.get(link)
        if req.status_code == 200:
            with open(outfile, 'w') as f:
                f.write(req.text)
            log.debug('Loaded and saved {} to {}'.format(link, outfile))
        else:
            log.error('{}: request error {}'.format(link, req.status_code))
    return outfile