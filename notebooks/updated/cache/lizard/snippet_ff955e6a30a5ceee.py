def outputmap(self, data):
    if isinstance(data, list):
        for item in data:
            self.outputmap(item)
    elif isinstance(data, dict):
        for map_target in self.output_map:
            if map_target in data:
                data[map_target] = getattr(self, self.output_map[map_target])(
                    data[map_target])
        for item in data.values():
            self.outputmap(item)