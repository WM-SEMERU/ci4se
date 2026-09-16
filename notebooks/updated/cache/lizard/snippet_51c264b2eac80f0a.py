def _from_binary_sec_desc(cls, binary_stream):
    header = SecurityDescriptorHeader.create_from_binary(binary_stream[:
        SecurityDescriptorHeader.get_representation_size()])
    owner_sid = SID.create_from_binary(binary_stream[header.owner_sid_offset:])
    group_sid = SID.create_from_binary(binary_stream[header.group_sid_offset:])
    dacl = None
    sacl = None
    if header.sacl_offset:
        sacl = ACL.create_from_binary(binary_stream[header.sacl_offset:])
    if header.dacl_offset:
        dacl = ACL.create_from_binary(binary_stream[header.dacl_offset:])
    nw_obj = cls((header, owner_sid, group_sid, sacl, dacl))
    return nw_obj