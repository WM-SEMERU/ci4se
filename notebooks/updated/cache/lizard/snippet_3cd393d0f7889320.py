def results(self, trial_ids):
    metadata_folder = os.path.join(self.log_dir, constants.METADATA_FOLDER)
    dfs = []
    for trial_id in trial_ids:
        result_file = os.path.join(metadata_folder, trial_id + '_' +
            constants.RESULT_SUFFIX)
        assert os.path.isfile(result_file), result_file
        dfs.append(pd.read_json(result_file, typ='frame', lines=True))
    df = pd.concat(dfs, axis=0, ignore_index=True, sort=False)
    return df