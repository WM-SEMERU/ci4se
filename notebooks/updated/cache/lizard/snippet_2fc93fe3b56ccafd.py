def decode_char_spot(raw_string):
    data = {}
    if re.match('[A-Za-z0-9\\/]+[:$]', raw_string[6:15]):
        data[const.SPOTTER] = re.sub(':', '', re.match(
            '[A-Za-z0-9\\/]+[:$]', raw_string[6:15]).group(0))
    else:
        raise ValueError
    if re.search('[0-9\\.]{5,12}', raw_string[10:25]):
        data[const.FREQUENCY] = float(re.search('[0-9\\.]{5,12}',
            raw_string[10:25]).group(0))
    else:
        raise ValueError
    data[const.DX] = re.sub('[^A-Za-z0-9\\/]+', '', raw_string[26:38])
    data[const.COMMENT] = re.sub(
        '[^\\sA-Za-z0-9\\.,;\\#\\+\\-!\\?\\$\\(\\)@\\/]+', ' ', raw_string[
        39:69]).strip()
    data[const.TIME] = datetime.now().replace(tzinfo=UTC)
    return data