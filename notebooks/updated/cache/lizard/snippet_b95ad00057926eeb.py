def get_encoders(encoder_num, input_layer, head_num, hidden_dim,
    attention_activation=None, feed_forward_activation='relu', dropout_rate
    =0.0, trainable=True):
    last_layer = input_layer
    for i in range(encoder_num):
        last_layer = get_encoder_component(name='Encoder-%d' % (i + 1),
            input_layer=last_layer, head_num=head_num, hidden_dim=
            hidden_dim, attention_activation=attention_activation,
            feed_forward_activation=feed_forward_activation, dropout_rate=
            dropout_rate, trainable=trainable)
    return last_layer