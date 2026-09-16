def get_per_pixel_mean(self, size=None):
    if self.caffepb is None:
        self.caffepb = get_caffe_pb()
    obj = self.caffepb.BlobProto()
    mean_file = os.path.join(self.dir, 'imagenet_mean.binaryproto')
    with open(mean_file, 'rb') as f:
        obj.ParseFromString(f.read())
    arr = np.array(obj.data).reshape((3, 256, 256)).astype('float32')
    arr = np.transpose(arr, [1, 2, 0])
    if size is not None:
        arr = cv2.resize(arr, size[::-1])
    return arr