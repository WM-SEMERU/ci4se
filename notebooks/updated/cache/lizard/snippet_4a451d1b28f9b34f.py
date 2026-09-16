def predict_topk(self, dataset, output_type='probability', k=3, verbose=
    True, batch_size=64):
    prob_vector = self.predict(dataset, output_type='probability_vector',
        verbose=verbose, batch_size=64)
    id_to_label = self._id_to_class_label
    if output_type == 'probability':
        results = prob_vector.apply(lambda p: [{'class': id_to_label[i],
            'probability': p[i]} for i in reversed(_np.argsort(p)[-k:])])
    else:
        assert output_type == 'rank'
        results = prob_vector.apply(lambda p: [{'class': id_to_label[i],
            'rank': rank} for rank, i in enumerate(reversed(_np.argsort(p)[
            -k:]))])
    results = _tc.SFrame({'X': results})
    results = results.add_row_number()
    results = results.stack('X', new_column_name='X')
    results = results.unpack('X', column_name_prefix='')
    return results