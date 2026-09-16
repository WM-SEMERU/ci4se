def edges_to_polygons(edges, vertices):
    polygons = []
    for dfs in graph.traversals(edges, mode='dfs'):
        try:
            polygons.append(repair_invalid(Polygon(vertices[dfs])))
        except ValueError:
            continue
    if len(polygons) == 1:
        return polygons
    roots, tree = enclosure_tree(polygons)
    complete = []
    for root in roots:
        interior = list(tree[root].keys())
        shell = polygons[root].exterior.coords
        holes = [polygons[i].exterior.coords for i in interior]
        complete.append(Polygon(shell=shell, holes=holes))
    return complete