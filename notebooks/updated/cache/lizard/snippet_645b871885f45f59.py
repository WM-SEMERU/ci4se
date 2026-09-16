def toTFExample(image, label):
    example = tf.train.Example(features=tf.train.Features(feature={'label':
        tf.train.Feature(int64_list=tf.train.Int64List(value=label.astype(
        'int64'))), 'image': tf.train.Feature(int64_list=tf.train.Int64List
        (value=image.astype('int64')))}))
    return example.SerializeToString()