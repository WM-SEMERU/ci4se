def _get_cifar(directory, url):
    filename = os.path.basename(url)
    path = generator_utils.maybe_download(directory, filename, url)
    tarfile.open(path, 'r:gz').extractall(directory)