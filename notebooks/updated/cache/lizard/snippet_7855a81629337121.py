def fits(A, B, temp, cos_distance):
    if cos_distance:
        distance_matrix = SNNLCrossEntropy.pairwise_cos_distance(A, B)
    else:
        distance_matrix = SNNLCrossEntropy.pairwise_euclid_distance(A, B)
    return tf.exp(-(distance_matrix / temp))