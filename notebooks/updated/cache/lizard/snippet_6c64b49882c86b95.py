def write_resources(self, resources):
    for filename, data in list(resources.get('outputs', {}).items()):
        dest = os.path.join(self.output_dir, filename)
        path = os.path.dirname(dest)
        if path and not os.path.isdir(path):
            os.makedirs(path)
        with open(dest, 'wb') as f:
            f.write(data)