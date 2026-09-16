def dist_calc(surf, cortex, source_nodes):
    cortex_vertices, cortex_triangles = surf_keep_cortex(surf, cortex)
    translated_source_nodes = translate_src(source_nodes, cortex)
    data = gdist.compute_gdist(cortex_vertices, cortex_triangles,
        source_indices=translated_source_nodes)
    dist = recort(data, surf, cortex)
    del data
    return dist