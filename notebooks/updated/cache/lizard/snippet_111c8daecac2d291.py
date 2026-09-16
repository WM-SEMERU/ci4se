def _fix_install_dir_for_user_site(self):
    if not self.user or not site.ENABLE_USER_SITE:
        return
    self.create_home_path()
    if self.install_userbase is None:
        msg = 'User base directory is not specified'
        raise DistutilsPlatformError(msg)
    self.install_base = self.install_platbase = self.install_userbase
    scheme_name = os.name.replace('posix', 'unix') + '_user'
    self.select_scheme(scheme_name)