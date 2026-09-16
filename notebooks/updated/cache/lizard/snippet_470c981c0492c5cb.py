def _get_vqa_v2_image_raw_dataset(directory, image_root_url, image_urls):
    for url in image_urls:
        filename = os.path.basename(url)
        download_url = os.path.join(image_root_url, url)
        path = generator_utils.maybe_download(directory, filename, download_url
            )
        unzip_dir = os.path.join(directory, filename.strip('.zip'))
        if not tf.gfile.Exists(unzip_dir):
            zipfile.ZipFile(path, 'r').extractall(directory)