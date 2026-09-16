def _extract_docs_other(self):
    if self.dst.style['in'] == 'numpydoc':
        data = '\n'.join([d.rstrip().replace(self.docs['out']['spaces'], '',
            1) for d in self.docs['in']['raw'].splitlines()])
        lst = self.dst.numpydoc.get_list_key(data, 'also')
        lst = self.dst.numpydoc.get_list_key(data, 'ref')
        lst = self.dst.numpydoc.get_list_key(data, 'note')
        lst = self.dst.numpydoc.get_list_key(data, 'other')
        lst = self.dst.numpydoc.get_list_key(data, 'example')
        lst = self.dst.numpydoc.get_list_key(data, 'attr')