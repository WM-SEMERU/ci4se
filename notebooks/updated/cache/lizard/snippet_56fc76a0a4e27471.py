def restore_from_object(self, obj):
    info = pickle.loads(obj)
    data = info['data']
    tmpdir = tempfile.mkdtemp('restore_from_object', dir=self.logdir)
    checkpoint_path = os.path.join(tmpdir, info['checkpoint_name'])
    for file_name, file_contents in data.items():
        with open(os.path.join(tmpdir, file_name), 'wb') as f:
            f.write(file_contents)
    self.restore(checkpoint_path)
    shutil.rmtree(tmpdir)