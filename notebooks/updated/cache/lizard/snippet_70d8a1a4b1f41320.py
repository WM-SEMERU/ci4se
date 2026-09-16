def _generate_relative_positions_matrix(length_q, length_k,
    max_relative_position, cache=False):
    if not cache:
        if length_q == length_k:
            range_vec_q = range_vec_k = tf.range(length_q)
        else:
            range_vec_k = tf.range(length_k)
            range_vec_q = range_vec_k[-length_q:]
        distance_mat = range_vec_k[(None), :] - range_vec_q[:, (None)]
    else:
        distance_mat = tf.expand_dims(tf.range(-length_k + 1, 1, 1), 0)
    distance_mat_clipped = tf.clip_by_value(distance_mat, -
        max_relative_position, max_relative_position)
    final_mat = distance_mat_clipped + max_relative_position
    return final_mat