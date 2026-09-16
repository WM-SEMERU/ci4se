def read_surfrad(filename, map_variables=True):
    if filename.startswith('ftp'):
        req = Request(filename)
        response = urlopen(req)
        file_buffer = io.StringIO(response.read().decode(errors='ignore'))
    else:
        file_buffer = open(filename, 'r')
    station = file_buffer.readline()
    file_metadata = file_buffer.readline()
    metadata_list = file_metadata.split()
    metadata = {}
    metadata['name'] = station.strip()
    metadata['latitude'] = float(metadata_list[0])
    metadata['longitude'] = float(metadata_list[1])
    metadata['elevation'] = float(metadata_list[2])
    metadata['surfrad_version'] = int(metadata_list[-1])
    metadata['tz'] = 'UTC'
    data = pd.read_csv(file_buffer, delim_whitespace=True, header=None,
        names=SURFRAD_COLUMNS)
    file_buffer.close()
    data = format_index(data)
    missing = data == -9999.9
    data = data.where(~missing, np.NaN)
    if map_variables:
        data.rename(columns=VARIABLE_MAP, inplace=True)
    return data, metadata