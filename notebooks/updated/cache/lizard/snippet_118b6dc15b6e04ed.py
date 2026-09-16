def download(self, url, save_path, header={}, redownload=False):
    if save_path is None:
        logger.error('save_path cannot be None')
        return None
    header = self.get_headers()
    if len(header) > 0:
        header.update(header)
    logger.debug('Download {url} to {save_path}'.format(url=url, save_path=
        save_path))
    save_location = cutil.norm_path(save_path)
    if redownload is False:
        if os.path.isfile(save_location):
            logger.debug('File {save_location} already exists'.format(
                save_location=save_location))
            return save_location
    cutil.create_path(save_location)
    if url.startswith('//'):
        url = 'http:' + url
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=header)
            ) as response, open(save_location, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
    except urllib.error.HTTPError as e:
        save_location = None
        if e.code != 404:
            logger.exception('Download Http Error {url}'.format(url=url))
    except Exception:
        save_location = None
        logger.exception('Download Error: {url}'.format(url=url))
    return save_location