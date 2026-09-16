def main():
    parser = argparse.ArgumentParser(description=
        'Tool for testing caffe to mxnet conversion layer by layer')
    parser.add_argument('--image_url', type=str, default=
        'https://github.com/dmlc/web-data/raw/master/mxnet/doc/tutorials/python/predict_image/cat.jpg'
        , help='input image to test inference, can be either file path or url')
    parser.add_argument('--caffe_prototxt_path', type=str, default=
        './model.prototxt', help='path to caffe prototxt')
    parser.add_argument('--caffe_model_path', type=str, default=
        './model.caffemodel', help='path to caffe weights')
    parser.add_argument('--caffe_mean', type=str, default=
        './model_mean.binaryproto', help='path to caffe mean file')
    parser.add_argument('--mean_diff_allowed', type=int, default=0.001,
        help='mean difference allowed between caffe blob and mxnet blob')
    parser.add_argument('--max_diff_allowed', type=int, default=0.1, help=
        'max difference allowed between caffe blob and mxnet blob')
    parser.add_argument('--gpu', type=int, default=-1, help=
        'the gpu id used for predict')
    args = parser.parse_args()
    convert_and_compare_caffe_to_mxnet(args.image_url, args.gpu, args.
        caffe_prototxt_path, args.caffe_model_path, args.caffe_mean, args.
        mean_diff_allowed, args.max_diff_allowed)