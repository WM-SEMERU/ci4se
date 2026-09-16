def trim_dict(data, max_dict_bytes, percent=50.0, stepper_size=10,
    replace_with='VALUE_TRIMMED', is_msgpacked=False, use_bin_type=False):
    serializer = salt.payload.Serial({'serial': 'msgpack'})
    if is_msgpacked:
        dict_size = sys.getsizeof(data)
    else:
        dict_size = sys.getsizeof(serializer.dumps(data))
    if dict_size > max_dict_bytes:
        if is_msgpacked:
            if use_bin_type:
                data = serializer.loads(data, encoding='utf-8')
            else:
                data = serializer.loads(data)
        while True:
            percent = float(percent)
            max_val_size = float(max_dict_bytes * (percent / 100))
            try:
                for key in data:
                    if isinstance(data[key], dict):
                        _trim_dict_in_dict(data[key], max_val_size,
                            replace_with)
                    elif sys.getsizeof(data[key]) > max_val_size:
                        data[key] = replace_with
                percent = percent - stepper_size
                max_val_size = float(max_dict_bytes * (percent / 100))
                if use_bin_type:
                    dump_data = serializer.dumps(data, use_bin_type=True)
                else:
                    dump_data = serializer.dumps(data)
                cur_dict_size = sys.getsizeof(dump_data)
                if cur_dict_size < max_dict_bytes:
                    if is_msgpacked:
                        return dump_data
                    else:
                        return data
                elif max_val_size == 0:
                    if is_msgpacked:
                        return dump_data
                    else:
                        return data
            except ValueError:
                pass
        if is_msgpacked:
            if use_bin_type:
                return serializer.dumps(data, use_bin_type=True)
            else:
                return serializer.dumps(data)
        else:
            return data
    else:
        return data