def create_simple_web_feature(o):
    try:
        id = o['id']
        g = o['geometry']
        p = o['properties']
        return SimpleWebFeature(str(id), {'type': str(g.get('type')),
            'coordinates': g.get('coordinates', [])}, title=p.get('title'),
            summary=p.get('summary'), link=str(p.get('link')))
    except (KeyError, TypeError):
        pass
    return o