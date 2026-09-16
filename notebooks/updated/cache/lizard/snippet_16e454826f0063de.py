def fiemap(fd):
    count = 72
    fiemap_cbuf = ffi.new('char[]', ffi.sizeof('struct fiemap') + count *
        ffi.sizeof('struct fiemap_extent'))
    fiemap_pybuf = ffi.buffer(fiemap_cbuf)
    fiemap_ptr = ffi.cast('struct fiemap*', fiemap_cbuf)
    assert ffi.sizeof(fiemap_cbuf) <= 4096
    while True:
        fiemap_ptr.fm_length = lib.FIEMAP_MAX_OFFSET
        fiemap_ptr.fm_extent_count = count
        fcntl.ioctl(fd, lib.FS_IOC_FIEMAP, fiemap_pybuf)
        if fiemap_ptr.fm_mapped_extents == 0:
            break
        for i in range(fiemap_ptr.fm_mapped_extents):
            extent = fiemap_ptr.fm_extents[i]
            yield FiemapExtent(extent.fe_logical, extent.fe_physical,
                extent.fe_length, extent.fe_flags)
        fiemap_ptr.fm_start = extent.fe_logical + extent.fe_length