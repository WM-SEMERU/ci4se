def inputs(dataset, batch_size=None, num_preprocess_threads=None):
    if not batch_size:
        batch_size = FLAGS.batch_size
    with tf.device('/cpu:0'):
        images, labels = batch_inputs(dataset, batch_size, train=False,
            num_preprocess_threads=num_preprocess_threads, num_readers=1)
    return images, labels