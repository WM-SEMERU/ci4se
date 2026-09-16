def __process_results(results):
    if 'no match' in results and 'returning 0 elements' in results:
        return []
    result_list = []
    split = results.split(sep='\n\n')[1:-1]
    for entry in split:
        entry_dict = {}
        for value in entry.split('\n'):
            if len(value) < 1:
                continue
            desc, val = value.split(': ')
            entry_dict[desc.replace('-', '')] = val.strip(' ')
        result_list.append(entry_dict)
    return result_list