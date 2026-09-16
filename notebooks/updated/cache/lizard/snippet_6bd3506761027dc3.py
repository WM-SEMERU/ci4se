def write_data(hyper_params, mode, sequence, num_threads):
    if not isinstance(sequence, Sequence) and not (callable(getattr(
        sequence, '__getitem__', None)) and callable(getattr(sequence,
        '__len__', None))):
        raise ValueError(
            'sequence must be tf.keras.utils.Sequence or a subtype or implement __len__(self) and __getitem__(self, idx)'
            )
    prefix = os.path.join(hyper_params.train.get('tf_records_path',
        'tfrecords'), mode)
    prefix = prefix.replace('\\', '/')
    data_tmp_folder = '/'.join(prefix.split('/')[:-1])
    if not os.path.exists(data_tmp_folder):
        os.makedirs(data_tmp_folder)
    args = [(hyper_params, sequence, num_threads, i, (prefix +
        '_%d.tfrecords') % i) for i in range(num_threads)]
    sample_feature, sample_label = sequence[0]
    config = {'num_threads': num_threads}
    for k in sample_feature.keys():
        config['feature_' + k] = {'shape': sample_feature[k].shape[1:],
            'dtype': sample_feature[k].dtype.name}
    for k in sample_label.keys():
        config['label_' + k] = {'shape': sample_label[k].shape[1:], 'dtype':
            sample_label[k].dtype.name}
    with open(prefix + '_config.json', 'w') as outfile:
        json.dump(config, outfile)
    pool = Pool(processes=num_threads)
    pool.map(_write_tf_record_pool_helper, args)