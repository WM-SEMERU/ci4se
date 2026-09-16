def get_variable(name, temp_s):
    return tf.Variable(tf.zeros(temp_s), name=name)