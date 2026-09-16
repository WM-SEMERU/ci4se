def _get_validation_labels(val_path):
    labels_path = tfds.core.get_tfds_path(_VALIDATION_LABELS_FNAME)
    with tf.io.gfile.GFile(labels_path) as labels_f:
        labels = labels_f.read().strip().split('\n')
    with tf.io.gfile.GFile(val_path, 'rb') as tar_f_obj:
        tar = tarfile.open(mode='r:', fileobj=tar_f_obj)
        images = sorted(tar.getnames())
    return dict(zip(images, labels))