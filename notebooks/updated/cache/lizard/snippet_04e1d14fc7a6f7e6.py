def load_img(self, img_path):
    with open_file(self.uuid, img_path) as f:
        return mpimg.imread(f)