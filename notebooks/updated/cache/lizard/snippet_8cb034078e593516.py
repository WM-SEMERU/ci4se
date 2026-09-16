def download_file(url, output_path):
    output_path = op.realpath(output_path)
    assert output_path is not None
    if op.exists(output_path):
        checked = _check_md5_of_url(output_path, url)
        if checked is False:
            logger.debug(
                'The file `%s` already exists but is invalid: redownloading.',
                output_path)
        elif checked is True:
            logger.debug('The file `%s` already exists: skipping.', output_path
                )
            return output_path
    r = _download(url, stream=True)
    _save_stream(r, output_path)
    if _check_md5_of_url(output_path, url) is False:
        logger.debug("The checksum doesn't match: retrying the download.")
        r = _download(url, stream=True)
        _save_stream(r, output_path)
        if _check_md5_of_url(output_path, url) is False:
            raise RuntimeError(
                "The checksum of the downloaded file doesn't match the provided checksum."
                )
    return