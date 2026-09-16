def discriminator(self, imgs, y):
    yv = y
    y = tf.reshape(y, [-1, 1, 1, 10])
    with argscope(Conv2D, kernel_size=5, strides=1):
        l = LinearWrap(imgs).ConcatWith(tf.tile(y, [1, 28, 28, 1]), 3).Conv2D(
            'conv0', 11).tf.nn.leaky_relu().ConcatWith(tf.tile(y, [1, 14, 
            14, 1]), 3).Conv2D('conv1', 74).BatchNorm('bn1').tf.nn.leaky_relu(
            ).apply(batch_flatten).ConcatWith(yv, 1).FullyConnected('fc1', 
            1024, activation=tf.identity).BatchNorm('bn2').tf.nn.leaky_relu(
            ).ConcatWith(yv, 1).FullyConnected('fct', 1, activation=tf.identity
            )()
    return l