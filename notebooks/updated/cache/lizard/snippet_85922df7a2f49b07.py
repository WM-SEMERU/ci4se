def get_bbox(self):
    resource_list = self.get_resource()
    bounding_box = namedtuple('boundingbox', ['southlatitude',
        'westlongitude', 'northlatitude', 'eastlongitude'])
    try:
        return [bounding_box(*resource['bbox']) for resource in resource_list]
    except (KeyError, TypeError):
        try:
            if isinstance(resource_list, dict):
                resource_list = [resource_list]
            return [bounding_box(resource['BoundingBox']['SouthLatitude'],
                resource['BoundingBox']['WestLongitude'], resource[
                'BoundingBox']['NorthLatitude'], resource['BoundingBox'][
                'EastLongitude']) for resource in resource_list]
        except (KeyError, TypeError) as exc:
            print(exc)