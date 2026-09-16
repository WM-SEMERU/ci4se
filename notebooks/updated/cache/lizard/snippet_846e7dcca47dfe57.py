def create_labels(da, labels, locations, direction):
    fontsize = 9
    aux_transform = mtransforms.IdentityTransform()
    labels_box = MyAuxTransformBox(aux_transform)
    xs, ys = [0] * len(labels), locations
    ha, va = 'left', 'center'
    x1, y1 = 0, 0
    x2, y2 = 0, da.height
    if direction == 'horizontal':
        xs, ys = ys, xs
        ha, va = 'center', 'top'
        x2, y2 = da.width, 0
    txt1 = mtext.Text(x1, y1, '', horizontalalignment=ha, verticalalignment=va)
    txt2 = mtext.Text(x2, y2, '', horizontalalignment=ha, verticalalignment=va)
    labels_box.add_artist(txt1)
    labels_box.add_artist(txt2)
    legend_text = []
    for i, (x, y, text) in enumerate(zip(xs, ys, labels)):
        txt = mtext.Text(x, y, text, size=fontsize, horizontalalignment=ha,
            verticalalignment=va)
        labels_box.add_artist(txt)
        legend_text.append(txt)
    return labels_box, legend_text