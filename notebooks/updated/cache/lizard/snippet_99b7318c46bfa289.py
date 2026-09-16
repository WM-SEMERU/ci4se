def get_metadata_file_path(channeldir, filename):
    channelparentdir, channeldirname = os.path.split(channeldir)
    return os.path.join(channelparentdir, filename)