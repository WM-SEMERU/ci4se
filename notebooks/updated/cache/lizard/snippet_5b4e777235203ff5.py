def _update_ctx(self, attrs):
    for row_label, v in attrs.iterrows():
        for col_label, col in v.iteritems():
            i = self.index.get_indexer([row_label])[0]
            j = self.columns.get_indexer([col_label])[0]
            for pair in col.rstrip(';').split(';'):
                self.ctx[i, j].append(pair)