def draw_boundary_images(glf, glb, v, f, vpe, fpe, camera):
    glf.Clear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glb.Clear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    from opendr.geometry import TriNormals
    tn = TriNormals(v, f).r.reshape((-1, 3))
    campos = -cv2.Rodrigues(camera.rt.r)[0].T.dot(camera.t.r)
    rays_to_verts = v.reshape((-1, 3)) - row(campos)
    rays_to_faces = rays_to_verts[f[:, (0)]] + rays_to_verts[f[:, (1)]
        ] + rays_to_verts[f[:, (2)]]
    dps = np.sum(rays_to_faces * tn, axis=1)
    dps = dps[fpe[:, (0)]] * dps[fpe[:, (1)]]
    silhouette_edges = np.asarray(np.nonzero(dps <= 0)[0], np.uint32)
    non_silhouette_edges = np.nonzero(dps > 0)[0]
    lines_e = vpe[silhouette_edges]
    lines_v = v
    visibility = draw_edge_visibility(glb, lines_v, lines_e, f,
        hidden_wireframe=True)
    shape = visibility.shape
    visibility = visibility.ravel()
    visible = np.nonzero(visibility.ravel() != 4294967295)[0]
    visibility[visible] = silhouette_edges[visibility[visible]]
    result = visibility.reshape(shape)
    return result