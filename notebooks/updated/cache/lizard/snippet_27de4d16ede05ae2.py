def venn2_circles(subsets, normalize_to=1.0, alpha=1.0, color='black',
    linestyle='solid', linewidth=2.0, ax=None, **kwargs):
    if isinstance(subsets, dict):
        subsets = [subsets.get(t, 0) for t in ['10', '01', '11']]
    elif len(subsets) == 2:
        subsets = compute_venn2_subsets(*subsets)
    areas = compute_venn2_areas(subsets, normalize_to)
    centers, radii = solve_venn2_circles(areas)
    if ax is None:
        ax = gca()
    prepare_venn_axes(ax, centers, radii)
    result = []
    for c, r in zip(centers, radii):
        circle = Circle(c, r, alpha=alpha, edgecolor=color, facecolor=
            'none', linestyle=linestyle, linewidth=linewidth, **kwargs)
        ax.add_patch(circle)
        result.append(circle)
    return result