def hardlink(source, link_name):
    if sys.version_info < (3,) and platform.system() == 'Windows':
        import ctypes
        create_hard_link = ctypes.windll.kernel32.CreateHardLinkW
        create_hard_link.argtypes = [ctypes.c_wchar_p, ctypes.c_wchar_p,
            ctypes.c_void_p]
        create_hard_link.restype = ctypes.wintypes.BOOL
        res = create_hard_link(link_name, source, None)
        if res == 0:
            raise ctypes.WinError()
    else:
        try:
            os.link(source, link_name)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
            else:
                source_stat = os.stat(source)
                dest_stat = os.stat(link_name)
                if (source_stat.st_dev != dest_stat.st_dev or source_stat.
                    st_ino != dest_stat.st_ino):
                    raise