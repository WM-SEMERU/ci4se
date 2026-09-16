def _get_vqa_v2_annotations(directory, annotation_url, annotation_filename=
    'vqa_v2.tar.gz'):
    annotation_file = generator_utils.maybe_download_from_drive(directory,
        annotation_filename, annotation_url)
    with tarfile.open(annotation_file, 'r:gz') as annotation_tar:
        annotation_tar.extractall(directory)