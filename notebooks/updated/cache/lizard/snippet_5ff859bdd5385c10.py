def _delete_sbo_tar_gz(self):
    if not self.auto and os.path.isfile(self.meta.build_path + self.script):
        os.remove(self.meta.build_path + self.script)