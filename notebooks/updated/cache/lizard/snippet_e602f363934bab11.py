def get_version_requested(path):
    tf_version_path = os.path.join(path, TF_VERSION_FILENAME)
    if not os.path.isfile(tf_version_path):
        LOGGER.error(
            'Terraform install attempted and no %s file present to dictate the version. Please create it (e.g.  write "0.11.13" (without quotes) to the file and try again'
            , TF_VERSION_FILENAME)
        sys.exit(1)
    with open(tf_version_path, 'r') as stream:
        ver = stream.read().rstrip()
    return ver