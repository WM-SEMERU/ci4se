def experiments_fmri_download(self, experiment_id):
    fmri = self.experiments_fmri_get(experiment_id)
    if fmri is None:
        return None
    return FileInfo(fmri.upload_file, fmri.properties[datastore.
        PROPERTY_MIMETYPE], fmri.properties[datastore.PROPERTY_FILENAME])