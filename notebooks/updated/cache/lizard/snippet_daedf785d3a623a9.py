def accuracy(logits, labels):
    is_correct = tf.nn.in_top_k(logits, labels, 1)
    correct = tf.reduce_sum(tf.cast(is_correct, tf.int32))
    incorrect = tf.reduce_sum(tf.cast(tf.logical_not(is_correct), tf.int32))
    correct_count = tf.Variable(0, False)
    incorrect_count = tf.Variable(0, False)
    correct_count_update = tf.assign_add(correct_count, correct)
    incorrect_count_update = tf.assign_add(incorrect_count, incorrect)
    accuracy_op = tf.cast(correct_count, tf.float32) / tf.cast(
        correct_count + incorrect_count, tf.float32)
    return [correct_count_update, incorrect_count_update], accuracy_op