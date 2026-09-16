def _unzip(self, src, dst, scene, force_unzip=False):
    self.output('Unzipping %s - It might take some time' % scene, normal=
        True, arrow=True)
    try:
        if isdir(dst) and not force_unzip:
            self.output('%s is already unzipped.' % scene, normal=True,
                color='green', indent=1)
            return
        else:
            tar = tarfile.open(src, 'r')
            tar.extractall(path=dst)
            tar.close()
    except tarfile.ReadError:
        check_create_folder(dst)
        subprocess.check_call(['tar', '-xf', src, '-C', dst])