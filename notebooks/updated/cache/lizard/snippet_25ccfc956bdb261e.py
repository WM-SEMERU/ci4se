def set_keras_backend(backend=None, gpu_device_nums=None, num_threads=None):
    os.environ['KERAS_BACKEND'] = 'tensorflow'
    original_backend = backend
    if not backend:
        backend = 'tensorflow-default'
    if gpu_device_nums is not None:
        os.environ['CUDA_VISIBLE_DEVICES'] = ','.join([str(i) for i in
            gpu_device_nums])
    if backend == 'tensorflow-cpu' or gpu_device_nums == []:
        print('Forcing tensorflow/CPU backend.')
        os.environ['CUDA_VISIBLE_DEVICES'] = ''
        device_count = {'CPU': 1, 'GPU': 0}
    elif backend == 'tensorflow-gpu':
        print('Forcing tensorflow/GPU backend.')
        device_count = {'CPU': 0, 'GPU': 1}
    elif backend == 'tensorflow-default':
        print('Forcing tensorflow backend.')
        device_count = None
    else:
        raise ValueError('Unsupported backend: %s' % backend)
    import tensorflow
    from keras import backend as K
    if K.backend() == 'tensorflow':
        config = tensorflow.ConfigProto(device_count=device_count)
        config.gpu_options.allow_growth = True
        if num_threads:
            config.inter_op_parallelism_threads = num_threads
            config.intra_op_parallelism_threads = num_threads
        session = tensorflow.Session(config=config)
        K.set_session(session)
    elif original_backend or gpu_device_nums or num_threads:
        warnings.warn(
            'Only tensorflow backend can be customized. Ignoring  customization. Backend: %s'
             % K.backend())