def read_label(self, hemi, parc_type='aparc'):
    parc_file = self.dir / 'label' / (hemi + '.' + parc_type + '.annot')
    vert_val, region_color, region_name = read_annot(parc_file)
    region_name = [x.decode('utf-8') for x in region_name]
    return vert_val, region_color, region_name