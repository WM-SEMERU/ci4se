def sanity(request, sysmeta_pyxb):
    _does_not_contain_replica_sections(sysmeta_pyxb)
    _is_not_archived(sysmeta_pyxb)
    _obsoleted_by_not_specified(sysmeta_pyxb)
    if 'HTTP_VENDOR_GMN_REMOTE_URL' in request.META:
        return
    _has_correct_file_size(request, sysmeta_pyxb)
    _is_supported_checksum_algorithm(sysmeta_pyxb)
    _is_correct_checksum(request, sysmeta_pyxb)