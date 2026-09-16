def cluster_lengths(self):
    number_ones = dict()
    for vector in self.bitvectors:
        vec_len = 4 * (len(vector) // 4)
        if vec_len == 0:
            continue
        if vec_len not in number_ones:
            number_ones[vec_len] = [np.zeros(vec_len, dtype=int), 0]
        number_ones[vec_len][0] += vector[0:vec_len]
        number_ones[vec_len][1] += 1
    return {vl: np.vectorize(lambda x: x if x >= 0.5 else 1 - x)(
        number_ones[vl][0] / number_ones[vl][1]) for vl in number_ones if 
        number_ones[vl][1] >= self.MIN_MESSAGES_PER_CLUSTER}