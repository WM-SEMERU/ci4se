def get_temp_export_dir(timestamped_export_dir):
    dirname, basename = os.path.split(timestamped_export_dir)
    temp_export_dir = os.path.join(tf.compat.as_bytes(dirname), tf.compat.
        as_bytes('temp-{}'.format(basename)))
    return temp_export_dir