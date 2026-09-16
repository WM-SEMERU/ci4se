def dump_normals(dataset_dir, data_dir, dataset, root=None, compress=True):
    if root is None:
        root = {}
    normals = dataset.GetPointData().GetNormals()
    if normals:
        dumped_array = dump_data_array(dataset_dir, data_dir, normals, {},
            compress)
        root['pointData']['activeNormals'] = len(root['pointData']['arrays'])
        root['pointData']['arrays'].append({'data': dumped_array})