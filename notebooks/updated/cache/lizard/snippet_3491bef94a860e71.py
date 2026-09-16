def gather_lines(self):
    total_lines = 0
    for file in self.all_files:
        full_path = os.path.join(self.paths['role'], file)
        with open(full_path, 'r') as f:
            for line in f:
                total_lines += 1
        if full_path.endswith('.yml'):
            self.yaml_files.append(full_path)
    return total_lines