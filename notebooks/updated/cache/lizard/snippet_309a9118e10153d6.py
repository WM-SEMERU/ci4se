def convert_to_dataset(obj, *, group='posterior', coords=None, dims=None):
    inference_data = convert_to_inference_data(obj, group=group, coords=
        coords, dims=dims)
    dataset = getattr(inference_data, group, None)
    if dataset is None:
        raise ValueError(
            'Can not extract {group} from {obj}! See {filename} for other conversion utilities.'
            .format(group=group, obj=obj, filename=__file__))
    return dataset