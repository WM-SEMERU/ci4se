def parse_header(file_obj):
    if 'ply' not in str(file_obj.readline()):
        raise ValueError('not a ply file!')
    encoding = file_obj.readline().decode('utf-8').strip().lower()
    is_ascii = 'ascii' in encoding
    endian = ['<', '>'][int('big' in encoding)]
    elements = collections.OrderedDict()
    image_name = None
    while True:
        line = file_obj.readline()
        if line is None:
            raise ValueError('Header not terminated properly!')
        line = line.decode('utf-8').strip().split()
        if 'end_header' in line:
            break
        if 'element' in line[0]:
            name, length = line[1:]
            elements[name] = {'length': int(length), 'properties':
                collections.OrderedDict()}
        elif 'property' in line[0]:
            if len(line) == 3:
                dtype, field = line[1:]
                elements[name]['properties'][str(field)] = endian + dtypes[
                    dtype]
            elif 'list' in line[1]:
                dtype_count, dtype, field = line[2:]
                elements[name]['properties'][str(field)] = endian + dtypes[
                    dtype_count] + ', ($LIST,)' + endian + dtypes[dtype]
        elif 'TextureFile' in line:
            index = line.index('TextureFile') + 1
            if index < len(line):
                image_name = line[index]
    return elements, is_ascii, image_name