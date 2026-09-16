def unpack_glist(glist_ptr, cffi_type, transfer_full=True):
    current = glist_ptr
    while current:
        yield ffi.cast(cffi_type, current.data)
        if transfer_full:
            free(current.data)
        current = current.next
    if transfer_full:
        lib.g_list_free(glist_ptr)