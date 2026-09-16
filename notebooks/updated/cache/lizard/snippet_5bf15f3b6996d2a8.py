def execute(self, eopatch):
    if not eopatch.data:
        raise ValueError('EOPatch must contain some data feature')
    if self.data_feature in eopatch.data:
        new_data, rescale = self._downscaling(eopatch.data[self.
            data_feature], eopatch.meta_info)
        reference_shape = eopatch.data[self.data_feature].shape[:3]
    else:
        new_data, new_dates = self._make_request(eopatch.bbox, eopatch.
            meta_info, eopatch.timestamp)
        removed_frames = eopatch.consolidate_timestamps(new_dates)
        for rm_frame in removed_frames:
            LOGGER.warning(
                'Removed data for frame %s from eopatch due to unavailability of %s!'
                , str(rm_frame), self.data_feature)
        reference_shape = next(iter(eopatch.data.values())).shape[:3]
        rescale = self._get_rescale_factors(reference_shape[1:3], eopatch.
            meta_info)
    clf_probs_lr = self.classifier.get_cloud_probability_maps(new_data)
    clf_mask_lr = self.classifier.get_mask_from_prob(clf_probs_lr)
    clf_mask_hr = self._upsampling(clf_mask_lr, rescale, reference_shape,
        interp='nearest')
    eopatch.mask[self.cm_feature] = clf_mask_hr.astype(np.bool)
    if self.cprobs_feature is not None:
        clf_probs_hr = self._upsampling(clf_probs_lr, rescale,
            reference_shape, interp='linear')
        eopatch.data[self.cprobs_feature] = clf_probs_hr.astype(np.float32)
    return eopatch