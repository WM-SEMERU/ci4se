def _histogram_equalization_helper(valid_data, number_of_bins, clip_limit=
    None, slope_limit=None):
    temp_histogram, temp_bins = np.histogram(valid_data, number_of_bins)
    if clip_limit is not None:
        pixels_to_clip_at = int(clip_limit * (valid_data.size / float(
            number_of_bins)))
        mask_to_clip = temp_histogram > clip_limit
        temp_histogram[mask_to_clip] = pixels_to_clip_at
    cumulative_dist_function = temp_histogram.cumsum()
    if slope_limit is not None:
        pixel_height_limit = int(slope_limit * (valid_data.size / float(
            number_of_bins)))
        cumulative_excess_height = 0
        num_clipped_pixels = 0
        weight_metric = np.zeros(cumulative_dist_function.shape, dtype=float)
        for pixel_index in range(1, cumulative_dist_function.size):
            current_pixel_count = cumulative_dist_function[pixel_index]
            diff_from_acceptable = (current_pixel_count -
                cumulative_dist_function[pixel_index - 1] -
                pixel_height_limit - cumulative_excess_height)
            if diff_from_acceptable < 0:
                weight_metric[pixel_index] = abs(diff_from_acceptable)
            cumulative_excess_height += max(diff_from_acceptable, 0)
            cumulative_dist_function[pixel_index
                ] = current_pixel_count - cumulative_excess_height
            num_clipped_pixels = num_clipped_pixels + cumulative_excess_height
    cumulative_dist_function = (number_of_bins - 1
        ) * cumulative_dist_function / cumulative_dist_function[-1]
    return cumulative_dist_function, temp_bins