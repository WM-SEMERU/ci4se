def get_default_cam_pos(self):
    focal_pt = self.center
    return [np.array(rcParams['camera']['position']) + np.array(focal_pt),
        focal_pt, rcParams['camera']['viewup']]