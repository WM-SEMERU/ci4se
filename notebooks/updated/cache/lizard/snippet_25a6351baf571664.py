def get_real_layer_path(self, path):
    filename = path.split('/')[-1]
    local_path = path
    filetype = os.path.splitext(filename)[1]
    if re.match('^[a-zA-Z]+://', path):
        local_path = os.path.join(DATA_DIRECTORY, filename)
        if not os.path.exists(local_path):
            sys.stdout.write('* Downloading %s...\n' % filename)
            self.download_file(path, local_path)
        elif self.args.redownload:
            os.remove(local_path)
            sys.stdout.write('* Redownloading %s...\n' % filename)
            self.download_file(path, local_path)
    elif not os.path.exists(local_path):
        raise Exception('%s does not exist' % local_path)
    real_path = path
    if filetype == '.zip':
        slug = os.path.splitext(filename)[0]
        real_path = os.path.join(DATA_DIRECTORY, slug)
        if not os.path.exists(real_path):
            sys.stdout.write('* Unzipping...\n')
            self.unzip_file(local_path, real_path)
    return real_path