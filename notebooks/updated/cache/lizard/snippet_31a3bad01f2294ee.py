def read_seg(self, parc_type='aparc'):
    seg_file = self.dir / 'mri' / (parc_type + '+aseg.mgz')
    seg_mri = load(seg_file)
    seg_aff = seg_mri.affine
    seg_dat = seg_mri.get_data()
    return seg_dat, seg_aff