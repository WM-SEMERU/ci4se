def ListDirectoryAbsolute(directory):
    return (os.path.join(directory, path) for path in tf.io.gfile.listdir(
        directory))