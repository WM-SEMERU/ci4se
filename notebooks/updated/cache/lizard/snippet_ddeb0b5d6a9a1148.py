def _save_namepaths_bids_derivatives(self, f, tag, save_directory, suffix=None
    ):
    file_name = f.split('/')[-1].split('.')[0]
    if tag != '':
        tag = '_' + tag
    if suffix:
        file_name, _ = drop_bids_suffix(file_name)
        save_name = file_name + tag
        save_name += '_' + suffix
    else:
        save_name = file_name + tag
    paths_post_pipeline = f.split(self.pipeline)
    if self.pipeline_subdir:
        paths_post_pipeline = paths_post_pipeline[1].split(self.pipeline_subdir
            )[0]
    else:
        paths_post_pipeline = paths_post_pipeline[1].split(file_name)[0]
    base_dir = (self.BIDS_dir + '/derivatives/' + 'teneto_' + teneto.
        __version__ + '/' + paths_post_pipeline + '/')
    save_dir = base_dir + '/' + save_directory + '/'
    if not os.path.exists(save_dir):
        try:
            os.makedirs(save_dir)
        except:
            time.sleep(2)
    if not os.path.exists(self.BIDS_dir + '/derivatives/' + 'teneto_' +
        teneto.__version__ + '/dataset_description.json'):
        try:
            with open(self.BIDS_dir + '/derivatives/' + 'teneto_' + teneto.
                __version__ + '/dataset_description.json', 'w') as fs:
                json.dump(self.tenetoinfo, fs)
        except:
            time.sleep(2)
    return save_name, save_dir, base_dir