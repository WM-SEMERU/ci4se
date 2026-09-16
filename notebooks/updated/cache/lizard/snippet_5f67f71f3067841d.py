def _fetch(self):
    while True:
        url = self._to_fetch.get()
        try:
            if url:
                page = self.get_page(url)
                if page is None:
                    continue
                for link, rel in page.links:
                    if link not in self._seen:
                        self._seen.add(link)
                        if not self._process_download(link
                            ) and self._should_queue(link, url, rel):
                            logger.debug('Queueing %s from %s', link, url)
                            self._to_fetch.put(link)
        finally:
            self._to_fetch.task_done()
        if not url:
            break