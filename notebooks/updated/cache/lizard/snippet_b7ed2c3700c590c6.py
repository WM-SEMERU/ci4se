def get_attribute(library, session, attribute):
    attr = attributes.AttributesByID[attribute]
    datatype = getattr(types, attr.visa_type)
    if datatype == ViString:
        attribute_state = create_string_buffer(256)
        ret = library.viGetAttribute(session, attribute, attribute_state)
        return buffer_to_text(attribute_state), ret
    elif datatype == ViAUInt8:
        length = get_attribute(library, session, constants.
            VI_ATTR_USB_RECV_INTR_SIZE)
        attribute_state = (ViUInt8 * length)()
        ret = library.viGetAttribute(session, attribute, byref(attribute_state)
            )
        return list(attribute_state), ret
    else:
        attribute_state = datatype()
        ret = library.viGetAttribute(session, attribute, byref(attribute_state)
            )
        return attribute_state.value, ret