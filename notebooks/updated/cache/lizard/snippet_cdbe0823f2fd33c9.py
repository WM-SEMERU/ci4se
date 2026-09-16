def clean_workspace(self):
    if os.path.isdir(self._temp_workspace):
        shutil.rmtree(self._temp_workspace)