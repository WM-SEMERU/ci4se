def draw_polygon_with_info(ax, polygon, off_x=0, off_y=0):
    pts = np.array(polygon)[ConvexHull(polygon).vertices]
    for i, pt in enumerate(pts):
        ax.plot([pt[0], pts[(i + 1) % len(pts)][0]], [pt[1], pts[(i + 1) %
            len(pts)][1]], 'k-')
    avex, avey = np.mean(pts, axis=0)
    ax.annotate('area: {:.3f}'.format(geometry.area(pts)), xy=(avex + off_x,
        avey + off_y), fontsize=12)