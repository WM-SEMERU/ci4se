def validate_examples(example_file):

    def test_example(raw):
        example = tf.train.Example()
        example.ParseFromString(raw)
        pi = np.frombuffer(example.features.feature['pi'].bytes_list.value[
            0], np.float32)
        value = example.features.feature['outcome'].float_list.value[0]
        assert abs(pi.sum() - 1) < 0.0001, pi.sum()
        assert value in (-1, 1), value
    opts = tf.python_io.TFRecordOptions(tf.python_io.
        TFRecordCompressionType.ZLIB)
    for record in tqdm(tf.python_io.tf_record_iterator(example_file, opts)):
        test_example(record)