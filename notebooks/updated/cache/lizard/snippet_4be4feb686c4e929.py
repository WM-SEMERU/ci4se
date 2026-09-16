def get_caffe_pb():
    dir = get_dataset_path('caffe')
    caffe_pb_file = os.path.join(dir, 'caffe_pb2.py')
    if not os.path.isfile(caffe_pb_file):
        download(CAFFE_PROTO_URL, dir)
        assert os.path.isfile(os.path.join(dir, 'caffe.proto'))
        if sys.version_info.major == 3:
            cmd = 'protoc --version'
            version, ret = subproc_call(cmd, timeout=3)
            if ret != 0:
                sys.exit(1)
            try:
                version = version.decode('utf-8')
                version = float('.'.join(version.split(' ')[1].split('.')[:2]))
                assert version >= 2.7, 'Require protoc>=2.7 for Python3'
            except Exception:
                logger.exception('protoc --version gives: ' + str(version))
                raise
        cmd = 'cd {} && protoc caffe.proto --python_out .'.format(dir)
        ret = os.system(cmd)
        assert ret == 0, 'Command `{}` failed!'.format(cmd)
        assert os.path.isfile(caffe_pb_file), caffe_pb_file
    import imp
    return imp.load_source('caffepb', caffe_pb_file)