def _adb(self, commands):
    ctx = self.ctx
    ctx.prepare_build_environment(user_sdk_dir=self.sdk_dir, user_ndk_dir=
        self.ndk_dir, user_android_api=self.android_api, user_ndk_api=self.
        ndk_api)
    if platform in ('win32', 'cygwin'):
        adb = sh.Command(join(ctx.sdk_dir, 'platform-tools', 'adb.exe'))
    else:
        adb = sh.Command(join(ctx.sdk_dir, 'platform-tools', 'adb'))
    info_notify('Starting adb...')
    output = adb(*commands, _iter=True, _out_bufsize=1, _err_to_out=True)
    for line in output:
        sys.stdout.write(line)
        sys.stdout.flush()