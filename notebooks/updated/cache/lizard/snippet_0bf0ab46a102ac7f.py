def write(self, text, encoding='utf-8'):
    logger.info('Writing to %s' % self)
    with codecs.open(self.path, 'w', encoding) as fout:
        fout.write(text)