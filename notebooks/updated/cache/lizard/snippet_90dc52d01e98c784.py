def parse_yaml(self, y):
    self.x = int(y['x'])
    self.y = int(y['y'])
    self.height = int(y['height'])
    self.width = int(y['width'])
    self.direction = dir.from_string(y['direction'])
    return self