def find_resources(library, session, query):
    find_list = ViFindList()
    return_counter = ViUInt32()
    instrument_description = create_string_buffer(constants.VI_FIND_BUFLEN)
    ret = library.viFindRsrc(session, query, byref(find_list), byref(
        return_counter), instrument_description)
    return find_list, return_counter.value, buffer_to_text(
        instrument_description), ret