def browse_website(self, browser=None):
    if len(self.all_versions):
        metadata = self.pypi.release_data(self.project_name, self.
            all_versions[0])
        self.logger.debug('DEBUG: browser: %s' % browser)
        if metadata.has_key('home_page'):
            self.logger.info('Launching browser: %s' % metadata['home_page'])
            if browser == 'konqueror':
                browser = webbrowser.Konqueror()
            else:
                browser = webbrowser.get()
                browser.open(metadata['home_page'], 2)
            return 0
    self.logger.error('No homepage URL found.')
    return 1