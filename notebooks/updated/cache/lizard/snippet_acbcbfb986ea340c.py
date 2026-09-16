def camera_marker(camera, marker_height=0.4, origin_size=None):
    camera_transform = camera.transform
    if camera_transform is None:
        camera_transform = np.eye(4)
    meshes = [axis(origin_size=marker_height / 10.0)]
    meshes[0].apply_transform(camera_transform)
    try:
        from .path.exchange.load import load_path
    except ImportError:
        log.warning('unable to create FOV visualization!', exc_info=True)
        return meshes
    if origin_size is None:
        origin_size = marker_height / 10.0
    x = marker_height * np.tan(np.deg2rad(camera.fov[0]) / 2.0)
    y = marker_height * np.tan(np.deg2rad(camera.fov[1]) / 2.0)
    z = marker_height
    points = np.array([(0, 0, 0), (-x, -y, z), (x, -y, z), (x, y, z), (-x,
        y, z)], dtype=float)
    segments = np.column_stack((np.zeros_like(points), points)).reshape((-1, 3)
        )
    segments = np.vstack((segments, points[[1, 2, 2, 3, 3, 4, 4, 1]])).reshape(
        (-1, 2, 3))
    meshes.append(load_path(segments))
    meshes[-1].apply_transform(camera_transform)
    return meshes