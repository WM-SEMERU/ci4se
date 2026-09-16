def _read_projections(folder, indices):
    datasets = []
    file_names = sorted([f for f in os.listdir(folder) if f.endswith('.dcm')])
    if len(file_names) == 0:
        raise ValueError('No DICOM files found in {}'.format(folder))
    file_names = file_names[indices]
    data_array = None
    for i, file_name in enumerate(tqdm.tqdm(file_names,
        'Loading projection data')):
        dataset = dicom.read_file(folder + '/' + file_name)
        rows = dataset.NumberofDetectorRows
        cols = dataset.NumberofDetectorColumns
        hu_factor = dataset.HUCalibrationFactor
        rescale_intercept = dataset.RescaleIntercept
        rescale_slope = dataset.RescaleSlope
        proj_array = np.array(np.frombuffer(dataset.PixelData, 'H'), dtype=
            'float32')
        proj_array = proj_array.reshape([rows, cols], order='F').T
        proj_array *= rescale_slope
        proj_array += rescale_intercept
        proj_array /= hu_factor
        if data_array is None:
            data_array = np.empty((len(file_names), cols, rows), dtype=
                'float32')
        data_array[i] = proj_array[:, ::-1]
        datasets.append(dataset)
    return datasets, data_array