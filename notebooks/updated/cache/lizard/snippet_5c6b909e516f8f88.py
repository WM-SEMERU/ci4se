def load_image(self, idx):
    im = Image.open('{}/data/images/img_{}.png'.format(self.nyud_dir, idx))
    in_ = np.array(im, dtype=np.float32)
    in_ = in_[:, :, ::-1]
    in_ -= self.mean_bgr
    in_ = in_.transpose((2, 0, 1))
    return in_