def _download_wrapper(self, url, *args, **kwargs):
    try:
        return url, self._file_downloader.download(url, *args, **kwargs)
    except Exception as e:
        logging.error('AbstractDownloader: %s', traceback.format_exc())
        return url, e