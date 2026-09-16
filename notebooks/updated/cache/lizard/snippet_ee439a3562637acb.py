def update_jobdir(self, site):
    working_path = self.cfg.get_working_path()
    if not working_path.endswith('/'):
        working_path += '/'
    jobdirname = self.__scrapy_options['JOBDIRNAME']
    if not jobdirname.endswith('/'):
        jobdirname += '/'
    site_string = ''.join(site['url']) + self.crawler_name
    hashed = hashlib.md5(site_string.encode('utf-8'))
    self.__scrapy_options['JOBDIR'
        ] = working_path + jobdirname + hashed.hexdigest()