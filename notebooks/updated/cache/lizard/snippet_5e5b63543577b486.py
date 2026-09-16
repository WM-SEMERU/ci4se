def make_parcellation(data_path, parcellation, parc_type=None, parc_params=None
    ):
    if isinstance(parcellation, str):
        parcin = ''
        if '+' in parcellation:
            parcin = parcellation
            parcellation = parcellation.split('+')[0]
        if '+OH' in parcin:
            subcortical = True
        else:
            subcortical = None
        if '+SUIT' in parcin:
            cerebellar = True
        else:
            cerebellar = None
        if not parc_type or not parc_params:
            path = tenetopath[0] + '/data/parcellation_defaults/defaults.json'
            with open(path) as data_file:
                defaults = json.load(data_file)
        if not parc_type:
            parc_type = defaults[parcellation]['type']
            print('Using default parcellation type')
        if not parc_params:
            parc_params = defaults[parcellation]['params']
            print('Using default parameters')
    if parc_type == 'sphere':
        parcellation = load_parcellation_coords(parcellation)
        seed = NiftiSpheresMasker(np.array(parcellation), **parc_params)
        data = seed.fit_transform(data_path)
    elif parc_type == 'region':
        path = tenetopath[0] + '/data/parcellation/' + parcellation + '.nii.gz'
        region = NiftiLabelsMasker(path, **parc_params)
        data = region.fit_transform(data_path)
    else:
        raise ValueError('Unknown parc_type specified')
    if subcortical:
        subatlas = fetch_atlas_harvard_oxford('sub-maxprob-thr0-2mm')['maps']
        region = NiftiLabelsMasker(subatlas, **parc_params)
        data_sub = region.fit_transform(data_path)
        data = np.hstack([data, data_sub])
    if cerebellar:
        path = (tenetopath[0] +
            '/data/parcellation/Cerebellum-SUIT_space-MNI152NLin2009cAsym.nii.gz'
            )
        region = NiftiLabelsMasker(path, **parc_params)
        data_cerebellar = region.fit_transform(data_path)
        data = np.hstack([data, data_cerebellar])
    return data