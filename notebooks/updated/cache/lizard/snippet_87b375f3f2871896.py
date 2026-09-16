def start_crawler(self, index, daemonize=False):
    call_process = [sys.executable, self.__single_crawler, self.
        cfg_file_path, self.json_file_path, '%s' % index, '%s' % self.
        shall_resume, '%s' % daemonize]
    self.log.debug('Calling Process: %s', call_process)
    crawler = Popen(call_process, stderr=None, stdout=None)
    crawler.communicate()
    self.crawlers.append(crawler)