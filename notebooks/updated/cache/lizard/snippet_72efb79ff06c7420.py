def geometricBar(weights, alldistribT):
    assert len(weights) == alldistribT.shape[1]
    return np.exp(np.dot(np.log(alldistribT), weights.T))