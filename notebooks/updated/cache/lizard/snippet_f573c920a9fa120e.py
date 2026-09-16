def _parse_single_video(self, example_proto):
    context_features = {'game_duration_loops': tf.io.FixedLenFeature([1],
        tf.int64), 'game_duration_seconds': tf.io.FixedLenFeature([1], tf.
        float32), 'n_steps': tf.io.FixedLenFeature([1], tf.int64),
        'screen_size': tf.io.FixedLenFeature([2], tf.int64)}
    sequence_features = {'rgb_screen': tf.io.FixedLenSequenceFeature([], tf
        .string)}
    _, seq_feat = tf.io.parse_single_sequence_example(example_proto,
        context_features=context_features, sequence_features=sequence_features)
    video_frames = tf.map_fn(tf.image.decode_png, seq_feat['rgb_screen'],
        dtype=tf.uint8)
    return video_frames