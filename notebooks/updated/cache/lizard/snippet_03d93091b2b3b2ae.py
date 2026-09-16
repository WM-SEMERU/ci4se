def get_vector(self):
    vec = {}
    for dim in ['forbidden', 'required', 'permitted']:
        if self.survey[dim] is None:
            continue
        dim_vec = map(lambda x: (x['tag'], x['answer']), self.survey[dim])
        vec[dim] = dict(dim_vec)
    return vec