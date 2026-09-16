def vertex_to_face_color(vertex_colors, faces):
    vertex_colors = to_rgba(vertex_colors)
    face_colors = vertex_colors[faces].mean(axis=1)
    return face_colors.astype(np.uint8)