def triangles_keep_cortex(triangles, cortex):
    input_shape = triangles.shape
    triangle_is_in_cortex = np.all(np.reshape(np.in1d(triangles.ravel(),
        cortex), input_shape), axis=1)
    cortex_triangles_old = np.array(triangles[triangle_is_in_cortex], dtype
        =np.int32)
    new_index = np.digitize(cortex_triangles_old.ravel(), cortex, right=True)
    cortex_triangles = np.array(np.arange(len(cortex))[new_index].reshape(
        cortex_triangles_old.shape), dtype=np.int32)
    return cortex_triangles