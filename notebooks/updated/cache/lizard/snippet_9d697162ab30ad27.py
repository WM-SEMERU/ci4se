def _filtering_step(self, basename):
    name = ''.join(basename.split('.')[:-1])
    if basename.split('.')[-1] == 'wav':
        if self.get_verbosity():
            print('Found wave! Copying to {}/filtered/{}'.format(self.
                src_dir, basename))
        subprocess.Popen(['cp', '{}/{}.wav'.format(self.src_dir, name),
            '{}/filtered/{}.wav'.format(self.src_dir, name)],
            universal_newlines=True).communicate()