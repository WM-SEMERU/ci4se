def fill_subparser(subparser):
    filenames = ['train-images-idx3-ubyte.gz', 'train-labels-idx1-ubyte.gz',
        't10k-images-idx3-ubyte.gz', 't10k-labels-idx1-ubyte.gz']
    urls = [('http://yann.lecun.com/exdb/mnist/' + f) for f in filenames]
    subparser.set_defaults(urls=urls, filenames=filenames)
    return default_downloader