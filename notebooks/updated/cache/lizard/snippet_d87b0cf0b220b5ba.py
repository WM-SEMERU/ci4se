def dump_image_data(dataset_dir, data_dir, dataset, color_array_info, root=
    None, compress=True):
    if root is None:
        root = {}
    root['vtkClass'] = 'vtkImageData'
    container = root
    container['spacing'] = dataset.GetSpacing()
    container['origin'] = dataset.GetOrigin()
    container['extent'] = dataset.GetExtent()
    dump_all_arrays(dataset_dir, data_dir, dataset, container, compress)
    return root