def download_url(url, content_type=None, download_to_file=None, retry_count
    =10, timeout=10.0):
    if not download_to_file:
        download_to_file = safe_mkstemp(suffix='.tmp', prefix=
            'filedownloadutils_')
    try:
        if is_url_a_local_file(url):
            downloaded_file = download_local_file(url, download_to_file)
        else:
            downloaded_file = download_external_url(url, download_to_file,
                content_type=content_type, retry_count=retry_count, timeout
                =timeout)
    except InvenioFileDownloadError:
        raise
    return downloaded_file