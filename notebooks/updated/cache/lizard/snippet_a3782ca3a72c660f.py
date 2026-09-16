def atomic_write_string_to_file(filename, contents, overwrite):
    temp_pathname = tf.compat.as_bytes(filename) + tf.compat.as_bytes('.tmp'
        ) + tf.compat.as_bytes(uuid.uuid4().hex)
    with tf_v1.gfile.GFile(temp_pathname, mode='w') as f:
        f.write(contents)
    try:
        tf_v1.gfile.Rename(temp_pathname, filename, overwrite)
    except tf.errors.OpError:
        tf_v1.gfile.Remove(temp_pathname)
        raise