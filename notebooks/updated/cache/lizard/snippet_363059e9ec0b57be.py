def handle_starttag(self, tag, attrs):
    self.log.debug('Encountered a start tag: {0} {1}'.format(tag, attrs))
    if tag in self.sanitizelist:
        self.level += 1
        return
    if self.isNotPurify or tag in self.whitelist_keys:
        attrs = self.__attrs_str(tag, attrs)
        attrs = ' ' + attrs if attrs else ''
        tmpl = ('<%s%s />' if tag in self.unclosedTags and self.
            isStrictHtml else '<%s%s>')
        self.data.append(tmpl % (tag, attrs))