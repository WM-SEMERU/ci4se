def generate_dylib_load_command(header, libary_install_name):
    lc = None
    cmd = None
    for command, internal_cmd, data in header.commands:
        if command.cmd == LC_LOAD_DYLIB and isinstance(internal_cmd,
            dylib_command):
            lc = deepcopy(command)
            cmd = deepcopy(internal_cmd)
            break
    if not lc or not cmd:
        raise Exception(
            'Invalid Mach-O file. I mean, there must be at least one LC_LOAD_DYLIB load command.'
            )
        return None
    cmd.timestamp = 0
    cmd.current_version = cmd.compatibility_version = 4096
    base = sizeof(load_command) + sizeof(dylib_command)
    cmd.name = base
    align = 4 if header.header.magic == MH_MAGIC else 8
    aligned_name = libary_install_name + b'\x00' * (align - len(
        libary_install_name) % align)
    lc.cmdsize = base + len(aligned_name)
    return lc, cmd, aligned_name