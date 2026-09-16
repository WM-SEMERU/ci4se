def save_chkpt_vars(dic, path):
    logger.info('Variables to save to {}:'.format(path))
    keys = sorted(list(dic.keys()))
    logger.info(pprint.pformat(keys))
    assert not path.endswith('.npy')
    if path.endswith('.npz'):
        np.savez_compressed(path, **dic)
    else:
        with tf.Graph().as_default(), tf.Session() as sess:
            for k, v in six.iteritems(dic):
                k = get_op_tensor_name(k)[0]
                _ = tf.Variable(name=k, initial_value=v)
            sess.run(tf.global_variables_initializer())
            saver = tf.train.Saver()
            saver.save(sess, path, write_meta_graph=False)