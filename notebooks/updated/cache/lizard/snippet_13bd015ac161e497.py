def consolidate_subdivide_geometry(geometry, max_query_area_size):
    quadrat_width = math.sqrt(max_query_area_size)
    if not isinstance(geometry, (Polygon, MultiPolygon)):
        raise ValueError('Geometry must be a shapely Polygon or MultiPolygon')
    if isinstance(geometry, MultiPolygon) or isinstance(geometry, Polygon
        ) and geometry.area > max_query_area_size:
        geometry = geometry.convex_hull
    if geometry.area > max_query_area_size:
        geometry = quadrat_cut_geometry(geometry, quadrat_width=quadrat_width)
    if isinstance(geometry, Polygon):
        geometry = MultiPolygon([geometry])
    return geometry