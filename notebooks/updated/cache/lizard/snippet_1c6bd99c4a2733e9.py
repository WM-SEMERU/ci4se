def _load_calib_rigid(self, filename):
    filepath = os.path.join(self.calib_path, filename)
    data = utils.read_calib_file(filepath)
    return utils.transform_from_rot_trans(data['R'], data['T'])