def transform_tensor(self, tensor):
    dim = tensor.shape
    rank = len(dim)
    assert all([(i == 3) for i in dim])
    lc = string.ascii_lowercase
    indices = lc[:rank], lc[rank:2 * rank]
    einsum_string = ','.join([(a + i) for a, i in zip(*indices)])
    einsum_string += ',{}->{}'.format(*indices[::-1])
    einsum_args = [self.rotation_matrix] * rank + [tensor]
    return np.einsum(einsum_string, *einsum_args)