def prepare(self, data_batch, sparse_row_id_fn=None):
    super(SVRGModule, self).prepare(data_batch, sparse_row_id_fn=
        sparse_row_id_fn)
    self._mod_aux.prepare(data_batch, sparse_row_id_fn=sparse_row_id_fn)