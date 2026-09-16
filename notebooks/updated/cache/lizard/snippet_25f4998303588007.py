def get_us_midlatitude_cyclone_abi(base_dir='.', method=None, force=False):
    if method is None:
        method = 'gcsfs'
    if method not in ['gcsfs']:
        raise NotImplementedError(
            "Demo data download method '{}' not implemented yet.".format(
            method))
    from ._google_cloud_platform import get_bucket_files
    patterns = [
        'gs://gcp-public-data-goes-16/ABI-L1b-RadC/2019/073/00/*0002*.nc']
    subdir = os.path.join(base_dir, 'abi_l1b',
        '20190314_us_midlatitude_cyclone')
    _makedirs(subdir, exist_ok=True)
    filenames = get_bucket_files(patterns, subdir, force=force)
    assert len(filenames) == 16, 'Not all files could be downloaded'
    return filenames