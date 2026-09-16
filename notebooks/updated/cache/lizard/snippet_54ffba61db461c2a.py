def _magic_signature_files(self, system_only=False, user_only=False):
    files = []
    user_binarch = self._user_path(self.BINWALK_MAGIC_DIR, self.
        BINARCH_MAGIC_FILE)
    system_binarch = self._system_path(self.BINWALK_MAGIC_DIR, self.
        BINARCH_MAGIC_FILE)

    def list_files(dir_path):
        return [os.path.join(dir_path, x) for x in os.listdir(dir_path) if 
            not x.startswith('.')]
    if not system_only:
        user_dir = os.path.join(self.user_dir, self.BINWALK_USER_DIR, self.
            BINWALK_MAGIC_DIR)
        files += list_files(user_dir)
    if not user_only:
        system_dir = os.path.join(self.system_dir, self.BINWALK_MAGIC_DIR)
        files += list_files(system_dir)
    if user_binarch in files:
        files.remove(user_binarch)
    if system_binarch in files:
        files.remove(system_binarch)
    return files