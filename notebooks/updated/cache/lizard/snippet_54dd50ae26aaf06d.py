def zoomlevel(self):
    resources = self.get_resource()
    zoomlevel = namedtuple('zoomlevel', 'zoomLevel')
    try:
        return [zoomlevel(resource['zoomLevel']) for resource in resources]
    except TypeError:
        try:
            if isinstance(resources['ElevationData'], dict):
                return zoomlevel(resources['ElevationData']['ZoomLevel'])
        except KeyError:
            try:
                if isinstance(resources['SeaLevelData'], dict):
                    zoom = resources['SeaLevelData']['ZoomLevel']
                    return zoomlevel(zoom)
            except KeyError:
                print(KeyError)