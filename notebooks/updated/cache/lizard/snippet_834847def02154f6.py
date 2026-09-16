def EnumerateFilesystemsFromClient(args):
    del args
    filenames = ['/proc/mounts', '/etc/mtab']
    for filename in filenames:
        for device, fs_type, mnt_point in CheckMounts(filename):
            yield rdf_client_fs.Filesystem(mount_point=mnt_point, type=
                fs_type, device=device)