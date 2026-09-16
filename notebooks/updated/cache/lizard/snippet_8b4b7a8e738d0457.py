def cross_product_matrix(vec):
    return np.array([[0, -vec[2], vec[1]], [vec[2], 0, -vec[0]], [-vec[1],
        vec[0], 0]])