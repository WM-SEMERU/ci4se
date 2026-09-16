def get_string(ea):
    string_type = idc.GetStringType(idaapi.get_item_head(ea))
    if string_type is None:
        raise exceptions.SarkNoString('No string at 0x{:08X}'.format(ea))
    string = idc.GetString(ea, strtype=string_type)
    if not string:
        raise exceptions.SarkNoString('No string at 0x{:08X}'.format(ea))
    return string