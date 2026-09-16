def embedding_plot(ind, shap_values, feature_names=None, method='pca',
    alpha=1.0, show=True):
    if feature_names is None:
        feature_names = [(labels['FEATURE'] % str(i)) for i in range(
            shap_values.shape[1])]
    ind = convert_name(ind, shap_values, feature_names)
    if ind == 'sum()':
        cvals = shap_values.sum(1)
        fname = 'sum(SHAP values)'
    else:
        cvals = shap_values[:, (ind)]
        fname = feature_names[ind]
    if type(method) == str and method == 'pca':
        pca = sklearn.decomposition.PCA(2)
        embedding_values = pca.fit_transform(shap_values)
    elif hasattr(method, 'shape') and method.shape[1] == 2:
        embedding_values = method
    else:
        print('Unsupported embedding method:', method)
    pl.scatter(embedding_values[:, (0)], embedding_values[:, (1)], c=cvals,
        cmap=colors.red_blue, alpha=alpha, linewidth=0)
    pl.axis('off')
    cb = pl.colorbar()
    cb.set_label('SHAP value for\n' + fname, size=13)
    cb.outline.set_visible(False)
    pl.gcf().set_size_inches(7.5, 5)
    bbox = cb.ax.get_window_extent().transformed(pl.gcf().dpi_scale_trans.
        inverted())
    cb.ax.set_aspect((bbox.height - 0.7) * 10)
    cb.set_alpha(1)
    if show:
        pl.show()