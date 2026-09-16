def get_compliance_expansion(self):
    if not self.order <= 4:
        raise ValueError(
            'Compliance tensor expansion only supported for fourth-order and lower'
            )
    ce_exp = [ElasticTensor(self[0]).compliance_tensor]
    einstring = 'ijpq,pqrsuv,rskl,uvmn->ijklmn'
    ce_exp.append(np.einsum(einstring, -ce_exp[-1], self[1], ce_exp[-1],
        ce_exp[-1]))
    if self.order == 4:
        einstring_1 = 'pqab,cdij,efkl,ghmn,abcdefgh'
        tensors_1 = [ce_exp[0]] * 4 + [self[-1]]
        temp = -np.einsum(einstring_1, *tensors_1)
        einstring_2 = 'pqab,abcdef,cdijmn,efkl'
        einstring_3 = 'pqab,abcdef,efklmn,cdij'
        einstring_4 = 'pqab,abcdef,cdijkl,efmn'
        for es in [einstring_2, einstring_3, einstring_4]:
            temp -= np.einsum(es, ce_exp[0], self[-2], ce_exp[1], ce_exp[0])
        ce_exp.append(temp)
    return TensorCollection(ce_exp)