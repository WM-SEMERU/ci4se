def lstm_cell(hidden_size):
    return tf.contrib.rnn.LSTMCell(hidden_size, use_peepholes=True,
        state_is_tuple=True)