def load(self, path):
    folder, filename = os.path.split(path)
    name, extension = os.path.splitext(filename)
    return Costume(name, Image.load(path))