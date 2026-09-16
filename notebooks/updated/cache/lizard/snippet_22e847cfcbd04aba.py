def multibox(centers, pitch, colors=None):
    from . import primitives
    from .base import Trimesh
    b = primitives.Box(extents=[pitch, pitch, pitch])
    v = np.tile(centers, (1, len(b.vertices))).reshape((-1, 3))
    v += np.tile(b.vertices, (len(centers), 1))
    f = np.tile(b.faces, (len(centers), 1))
    f += np.tile(np.arange(len(centers)) * len(b.vertices), (len(b.faces), 1)
        ).T.reshape((-1, 1))
    face_colors = None
    if colors is not None:
        colors = np.asarray(colors)
        if colors.ndim == 1:
            colors = colors[None].repeat(len(centers), axis=0)
        if colors.ndim == 2 and len(colors) == len(centers):
            face_colors = colors.repeat(12, axis=0)
    mesh = Trimesh(vertices=v, faces=f, face_colors=face_colors)
    return mesh