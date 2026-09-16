def StatFSFromClient(args):
    if platform.system() == 'Windows':
        raise RuntimeError('os.statvfs not available on Windows')
    for path in args.path_list:
        try:
            fd = vfs.VFSOpen(rdf_paths.PathSpec(path=path, pathtype=args.
                pathtype))
            st = fd.StatFS()
            mount_point = fd.GetMountPoint()
        except (IOError, OSError):
            continue
        unix = rdf_client_fs.UnixVolume(mount_point=mount_point)
        yield rdf_client_fs.Volume(bytes_per_sector=st.f_frsize or st.
            f_bsize, sectors_per_allocation_unit=1, total_allocation_units=
            st.f_blocks, actual_available_allocation_units=st.f_bavail,
            unixvolume=unix)