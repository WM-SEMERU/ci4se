def grab_checksums_file(entry):
    http_url = convert_ftp_url(entry['ftp_path'])
    full_url = '{}/md5checksums.txt'.format(http_url)
    req = requests.get(full_url)
    return req.text