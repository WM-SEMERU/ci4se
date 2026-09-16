def write_input(self, output_dir='.', make_dir_if_not_present=True):
    if make_dir_if_not_present and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for k, v in self.items():
        with zopen(os.path.join(output_dir, k), 'wt') as f:
            f.write(v.__str__())