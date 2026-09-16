def remount_with_additional_flags(mountpoint, existing_options, mountflags):
    mountflags |= libc.MS_REMOUNT | libc.MS_BIND
    for option, flag in libc.MOUNT_FLAGS.items():
        if option in existing_options:
            mountflags |= flag
    libc.mount(None, mountpoint, None, mountflags, None)