def _generate_examples(self, data_path):
    with tf.io.gfile.GFile(data_path, 'rb') as fp:
        images = np.load(fp)
    images = np.transpose(images, (1, 0, 2, 3))
    images = np.expand_dims(images, axis=-1)
    for sequence in images:
        yield dict(image_sequence=sequence)