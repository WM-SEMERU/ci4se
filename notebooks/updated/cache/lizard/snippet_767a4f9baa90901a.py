def get_bucket(self, hash_name, bucket_key):
    results = []
    for row in self._get_bucket_rows(hash_name, bucket_key):
        val_dict = pickle.loads(row)
        if 'sparse' in val_dict:
            row = []
            col = []
            data = []
            for e in val_dict['nonzeros']:
                row.append(e[0])
                data.append(e[1])
                col.append(0)
            coo_row = numpy.array(row, dtype=numpy.int32)
            coo_col = numpy.array(col, dtype=numpy.int32)
            coo_data = numpy.array(data)
            vector = scipy.sparse.coo_matrix((coo_data, (coo_row, coo_col)),
                shape=(val_dict['dim'], 1))
        else:
            vector = numpy.fromstring(val_dict['vector'], dtype=val_dict[
                'dtype'])
        results.append((vector, val_dict.get('data')))
    return results