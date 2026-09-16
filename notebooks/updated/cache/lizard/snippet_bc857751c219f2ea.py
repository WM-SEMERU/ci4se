def import_obj(file_name, **kwargs):

    def default_callback(face_list):
        return face_list
    callback_func = kwargs.get('callback', default_callback)
    content = exch.read_file(file_name)
    content_arr = content.split('\n')
    on_face = False
    vertices = []
    triangles = []
    faces = []
    vert_idx = 1
    tri_idx = 1
    face_idx = 1
    for carr in content_arr:
        carr = carr.strip()
        data = carr.split(' ')
        data = [d.strip() for d in data]
        if data[0] == 'v':
            if on_face:
                on_face = not on_face
                face = elements.Face(*triangles, id=face_idx)
                faces.append(face)
                face_idx += 1
                vertices[:] = []
                triangles[:] = []
                vert_idx = 1
                tri_idx = 1
            vertex = elements.Vertex(*data[1:], id=vert_idx)
            vertices.append(vertex)
            vert_idx += 1
        if data[0] == 'f':
            on_face = True
            triangle = elements.Triangle(*[vertices[int(fidx) - 1] for fidx in
                data[1:]], id=tri_idx)
            triangles.append(triangle)
            tri_idx += 1
    if triangles:
        face = elements.Face(*triangles, id=face_idx)
        faces.append(face)
    return callback_func(faces)