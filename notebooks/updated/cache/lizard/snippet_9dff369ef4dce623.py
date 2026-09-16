def _modeldesc_from_dict(self, d):
    lhs_termlist = [Term([LookupFactor(d['lhs_termlist'][0])])]
    rhs_termlist = []
    for name in d['rhs_termlist']:
        if name == '':
            rhs_termlist.append(Term([]))
        else:
            rhs_termlist.append(Term([LookupFactor(name)]))
    md = ModelDesc(lhs_termlist, rhs_termlist)
    return md