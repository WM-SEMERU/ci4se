def download(timestamp, dataset, path=None, products=None, levels=None,
    offset=0):
    if path is None:
        path = DATA_PATH
    closest = timestamp.hour // 6 * 6
    filename = dataset(closest, offset)
    gfs_timestamp = '%s%02d' % (timestamp.strftime('%Y%m%d'), closest)
    url = baseurl(gfs_timestamp, filename)
    index = url + '.idx'
    messages = message_index(index)
    segments = _filter_messages(messages, products, levels)
    dl_path = path + '/%s/' % gfs_timestamp
    _verify_path(dl_path)
    _download_segments(path + filename, url, segments)