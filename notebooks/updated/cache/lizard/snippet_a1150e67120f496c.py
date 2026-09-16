def post_freeze_hook(self):
    if os.path.isdir(self._metadata_fragments_abspath):
        shutil.rmtree(self._metadata_fragments_abspath)