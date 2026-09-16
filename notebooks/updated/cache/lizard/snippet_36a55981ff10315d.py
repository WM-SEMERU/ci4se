def fetch():
    doi = '10.7910/DVN/AFJNWJ'
    fname = os.path.join(data_dir(), 'lenz2017', 'ebv_lhd.hpx.fits')
    fetch_utils.dataverse_download_doi(doi, fname, file_requirements={
        'filename': 'ebv_lhd.hpx.fits'})