def hybrid_forward(self, F, x, sampled_values, label, weight, bias):
    sampled_candidates, _, _ = sampled_values
    label = F.reshape(label, shape=(-1,))
    ids = F.concat(sampled_candidates, label, dim=0)
    w_all = F.Embedding(data=ids, weight=weight, input_dim=self.
        _num_classes, output_dim=self._in_unit, sparse_grad=self._sparse_grad)
    b_all = F.take(bias, indices=ids)
    return self._dense(x, sampled_values, label, w_all, b_all)