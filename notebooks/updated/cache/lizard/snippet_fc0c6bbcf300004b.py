def correlation_matrix(corrdf, title, **kwargs):
    imgdata = BytesIO()
    fig_cor, axes_cor = plt.subplots(1, 1)
    labels = corrdf.columns
    matrix_image = axes_cor.imshow(corrdf, vmin=-1, vmax=1, interpolation=
        'nearest', cmap='bwr')
    plt.title(title, size=18)
    plt.colorbar(matrix_image)
    axes_cor.set_xticks(np.arange(0, corrdf.shape[0], corrdf.shape[0] * 1.0 /
        len(labels)))
    axes_cor.set_yticks(np.arange(0, corrdf.shape[1], corrdf.shape[1] * 1.0 /
        len(labels)))
    axes_cor.set_xticklabels(labels, rotation=90)
    axes_cor.set_yticklabels(labels)
    matrix_image.figure.savefig(imgdata, bbox_inches='tight')
    imgdata.seek(0)
    result_string = 'data:image/png;base64,' + quote(base64.b64encode(
        imgdata.getvalue()))
    plt.close(matrix_image.figure)
    return result_string