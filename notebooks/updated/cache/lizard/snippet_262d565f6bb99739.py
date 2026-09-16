def download_previews(self, savedir=None):
    for obsid in self.obsids:
        pm = io.PathManager(obsid.img_id, savedir=savedir)
        pm.basepath.mkdir(exist_ok=True)
        basename = Path(obsid.medium_img_url).name
        print('Downloading', basename)
        urlretrieve(obsid.medium_img_url, str(pm.basepath / basename))