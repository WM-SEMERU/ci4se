def grab_zipped_url(zipped_url, ensure=True, appname='utool', download_dir=
    None, force_commonprefix=True, cleanup=False, redownload=False, spoof=False
    ):
    r
    zipped_url = clean_dropbox_link(zipped_url)
    zip_fname = split(zipped_url)[1]
    data_name = split_archive_ext(zip_fname)[0]
    if download_dir is None:
        download_dir = util_cplat.get_app_cache_dir(appname)
    data_dir = join(download_dir, data_name)
    if ensure or redownload:
        if redownload:
            util_path.remove_dirs(data_dir)
        util_path.ensurepath(download_dir)
        if not exists(data_dir) or redownload:
            zip_fpath = realpath(join(download_dir, zip_fname))
            if not exists(zip_fpath) or redownload:
                download_url(zipped_url, zip_fpath, spoof=spoof)
            unarchive_file(zip_fpath, force_commonprefix)
            if cleanup:
                util_path.delete(zip_fpath)
    if cleanup:
        util_path.assert_exists(data_dir)
    return util_path.unixpath(data_dir)