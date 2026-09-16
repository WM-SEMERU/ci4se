def sample_prob(probs, rand):
    return tf.nn.relu(tf.sign(probs - rand))