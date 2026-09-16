def create_pairwise_bilateral(sdims, schan, img, chdim=-1):
    if chdim == -1:
        im_feat = img[np.newaxis].astype(np.float32)
    else:
        im_feat = np.rollaxis(img, chdim).astype(np.float32)
    if isinstance(schan, Number):
        im_feat /= schan
    else:
        for i, s in enumerate(schan):
            im_feat[i] /= s
    cord_range = [range(s) for s in im_feat.shape[1:]]
    mesh = np.array(np.meshgrid(*cord_range, indexing='ij'), dtype=np.float32)
    for i, s in enumerate(sdims):
        mesh[i] /= s
    feats = np.concatenate([mesh, im_feat])
    return feats.reshape([feats.shape[0], -1])