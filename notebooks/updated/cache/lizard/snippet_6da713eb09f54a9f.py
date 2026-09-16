def _get_remote_ontology(onto_url, time_difference=None):
    if onto_url is None:
        return False
    dl_dir = os.path.join(current_app.config['CLASSIFIER_WORKDIR'] or
        tempfile.gettempdir(), 'classifier')
    if not os.path.exists(dl_dir):
        os.makedirs(dl_dir)
    local_file = dl_dir + os.path.basename(onto_url)
    remote_modif_time = _get_last_modification_date(onto_url)
    try:
        local_modif_seconds = os.path.getmtime(local_file)
    except OSError:
        download = True
        current_app.logger.info('The local ontology could not be found.')
    else:
        local_modif_time = datetime(*time.gmtime(local_modif_seconds)[0:6])
        time_difference = time_difference or timedelta(hours=1, minutes=10)
        download = remote_modif_time > local_modif_time + time_difference
        if download:
            current_app.logger.info(
                "The remote ontology '{0}' is more recent than the local ontology."
                .format(onto_url))
    if download:
        if not _download_ontology(onto_url, local_file):
            current_app.logger.warning(
                'Error downloading the ontology from: {0}'.format(onto_url))
    return local_file