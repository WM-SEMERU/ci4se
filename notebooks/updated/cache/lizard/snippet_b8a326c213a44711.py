def ReadIntoObject(buff, index, value_obj, length=0):
    raw_data = value_obj.GetRawData()
    count = 0
    for encoded_tag, encoded_length, encoded_field in SplitBuffer(buff,
        index=index, length=length):
        type_info_obj = value_obj.type_infos_by_encoded_tag.get(encoded_tag)
        wire_format = encoded_tag, encoded_length, encoded_field
        if type_info_obj is None:
            raw_data[count] = None, wire_format, None
            count += 1
        elif type_info_obj.__class__ is ProtoList:
            value_obj.Get(type_info_obj.name).wrapped_list.append((None,
                wire_format))
        else:
            raw_data[type_info_obj.name] = None, wire_format, type_info_obj
    value_obj.SetRawData(raw_data)