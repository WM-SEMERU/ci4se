def _csf_to_list(option):
    result = []
    line = get_option(option)
    if line:
        csv = line.split('=')[1].replace(' ', '').replace('"', '')
        result = csv.split(',')
    return result