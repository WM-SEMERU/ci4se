def _get_ftp(url, temp_file_name, initial_size, file_size, verbose_bool,
    progressbar, ncols=80):
    parsed_url = urllib.parse.urlparse(url)
    file_name = os.path.basename(parsed_url.path)
    server_path = parsed_url.path.replace(file_name, '')
    unquoted_server_path = urllib.parse.unquote(server_path)
    data = ftplib.FTP()
    if parsed_url.port is not None:
        data.connect(parsed_url.hostname, parsed_url.port)
    else:
        data.connect(parsed_url.hostname)
    data.login()
    if len(server_path) > 1:
        data.cwd(unquoted_server_path)
    data.sendcmd('TYPE I')
    data.sendcmd('REST ' + str(initial_size))
    down_cmd = 'RETR ' + file_name
    assert file_size == data.size(file_name)
    if progressbar:
        progress = tqdm(total=file_size, initial=initial_size, desc=
            'file_sizes', ncols=ncols, unit='B', unit_scale=True)
    else:
        progress = None
    mode = 'ab' if initial_size > 0 else 'wb'
    with open(temp_file_name, mode) as local_file:

        def chunk_write(chunk):
            return _chunk_write(chunk, local_file, progress)
        data.retrbinary(down_cmd, chunk_write)
        data.close()