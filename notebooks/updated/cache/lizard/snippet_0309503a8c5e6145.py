def move(self):
    if not os.path.isdir(self.outdir):
        os.makedirs(self.outdir)
    shutil.move(self.tmpdir, os.path.join(self.outdir, self.name))