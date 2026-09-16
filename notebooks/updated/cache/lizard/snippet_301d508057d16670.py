def make_edge_vectors(adjacency_matrix, num_edge_types, depth, name=None):
    with tf.variable_scope(name, default_name='edge_vectors'):
        att_adj_vectors_shape = [num_edge_types, depth]
        adjacency_matrix_shape = common_layers.shape_list(adjacency_matrix)
        adj_vectors = tf.get_variable('adj_vectors', att_adj_vectors_shape,
            initializer=tf.random_normal_initializer(0, depth ** -0.5)
            ) * depth ** 0.5
        adjacency_matrix_one_hot = tf.one_hot(adjacency_matrix, num_edge_types)
        att_adj_vectors = tf.matmul(tf.reshape(tf.to_float(
            adjacency_matrix_one_hot), [-1, num_edge_types]), adj_vectors)
        return tf.reshape(att_adj_vectors, [adjacency_matrix_shape[0],
            adjacency_matrix_shape[1], adjacency_matrix_shape[2], depth])