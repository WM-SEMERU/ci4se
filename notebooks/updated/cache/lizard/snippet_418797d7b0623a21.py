def _split_generators(self, dl_manager):
    cifar_path = dl_manager.download_and_extract(self._cifar_info.url)
    cifar_info = self._cifar_info
    cifar_path = os.path.join(cifar_path, cifar_info.prefix)
    for label_key, label_file in zip(cifar_info.label_keys, cifar_info.
        label_files):
        labels_path = os.path.join(cifar_path, label_file)
        with tf.io.gfile.GFile(labels_path) as label_f:
            label_names = [name for name in label_f.read().split('\n') if name]
        self.info.features[label_key].names = label_names

    def gen_filenames(filenames):
        for f in filenames:
            yield os.path.join(cifar_path, f)
    return [tfds.core.SplitGenerator(name=tfds.Split.TRAIN, num_shards=10,
        gen_kwargs={'filepaths': gen_filenames(cifar_info.train_files)}),
        tfds.core.SplitGenerator(name=tfds.Split.TEST, num_shards=1,
        gen_kwargs={'filepaths': gen_filenames(cifar_info.test_files)})]