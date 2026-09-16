def csv_dict_format(csv_data, c_headers=None, r_headers=None):
    if r_headers:
        result = {}
        for k_index in range(0, len(csv_data)):
            if r_headers[k_index]:
                result[r_headers[k_index]] = collections.OrderedDict(zip(
                    c_headers, csv_data[k_index]))
    else:
        result = []
        for k_index in range(0, len(csv_data)):
            result.append(collections.OrderedDict(zip(c_headers, csv_data[
                k_index])))
        result = [result]
    return result