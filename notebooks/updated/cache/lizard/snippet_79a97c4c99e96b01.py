def _read_checkpoint_vars(model_path):
    reader = tf.train.NewCheckpointReader(model_path)
    reader = CheckpointReaderAdapter(reader)
    ckpt_vars = reader.get_variable_to_shape_map().keys()
    return reader, set(ckpt_vars)