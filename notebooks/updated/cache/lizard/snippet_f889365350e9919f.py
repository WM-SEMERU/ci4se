def format(self, link_resolver, output, extensions):
    info('Formatting documentation tree', 'formatting')
    self.__setup_folder(output)
    link_resolver.get_link_signal.connect(self.__get_link_cb)
    self.__extensions = extensions
    for page in self.walk():
        self.format_page(page, link_resolver, output, extensions)
    self.__extensions = None
    link_resolver.get_link_signal.disconnect(self.__get_link_cb)