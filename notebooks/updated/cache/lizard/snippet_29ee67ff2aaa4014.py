def sign(self, storepass=None, keypass=None, keystore=None, apk=None, alias
    =None, name='app'):
    self.src_folder = self.get_src_folder()
    if keystore is None:
        keystore, storepass, keypass, alias = (android_helper.
            get_default_keystore())
    dist = '%s/%s.apk' % ('/'.join(apk.split('/')[:-1]), name)
    android_helper.jarsign(storepass, keypass, keystore, apk, alias, path=
        self.path)
    android_helper.zipalign(apk, dist, build_tool=self.
        get_build_tool_version(), path=self.path)