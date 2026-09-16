def likelihood(self, samples):
    ret = np.ones(NUM_OF_INSTANCE)
    for i in range(NUM_OF_INSTANCE):
        for j in range(1, self.point_num + 1):
            ret[i] *= self.normal_distribution(j, samples[i])
    return ret