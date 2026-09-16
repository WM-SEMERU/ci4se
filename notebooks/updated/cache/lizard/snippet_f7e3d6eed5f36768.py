def _reset_corpus_iterator(self):
    self.__context = etree.iterparse(self.urml_file, events=('end',), tag=
        'document', recover=False)