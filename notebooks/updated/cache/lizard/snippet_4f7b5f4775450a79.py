def add_transform_chain(self, tc):
    for t in tc.gpu_transforms:
        if isinstance(t, Clip):
            self.insert_vert('v_temp_pos_tr = temp_pos_tr;')
            continue
        self.insert_vert(t.glsl('temp_pos_tr'))
    clip = tc.get('Clip')
    if clip:
        self.insert_frag(clip.glsl('v_temp_pos_tr'), 'before_transforms')