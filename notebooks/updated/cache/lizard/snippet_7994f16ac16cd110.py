def load_glb(file_obj, resolver=None, **mesh_kwargs):
    start = file_obj.tell()
    head_data = file_obj.read(20)
    head = np.frombuffer(head_data, dtype='<u4')
    if head[0] != _magic['gltf'] or head[1] != 2:
        raise ValueError('file is not GLTF 2.0')
    length, chunk_length, chunk_type = head[2:]
    if chunk_type != _magic['json']:
        raise ValueError('no initial JSON header!')
    json_data = file_obj.read(int(chunk_length))
    if hasattr(json_data, 'decode'):
        json_data = json_data.decode('utf-8')
    header = json.loads(json_data)
    buffers = []
    while file_obj.tell() - start < length:
        chunk_head = file_obj.read(8)
        if len(chunk_head) != 8:
            break
        chunk_length, chunk_type = np.frombuffer(chunk_head, dtype='<u4')
        if chunk_type != _magic['bin']:
            raise ValueError('not binary GLTF!')
        chunk_data = file_obj.read(int(chunk_length))
        if len(chunk_data) != chunk_length:
            raise ValueError('chunk was not expected length!')
        buffers.append(chunk_data)
    kwargs = _read_buffers(header=header, buffers=buffers, mesh_kwargs=
        mesh_kwargs)
    return kwargs