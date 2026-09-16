def scatmat(df, category=None, colors='rgob', num_plots=4, num_topics=100,
    num_columns=4, show=False, block=False, data_path=DATA_PATH, save=False,
    verbose=1):
    if category is None:
        category = list(df.columns)[-1]
    if isinstance(category, (str, bytes, int)) and category in df.columns:
        category = df[category]
    else:
        category = pd.Series(category)
    suffix = '{}x{}'.format(*list(df.shape))
    for i in range(min(num_plots * num_columns, num_topics) / num_plots):
        scatter_matrix(df[df.columns[i * num_columns:(i + 1) * num_columns]
            ], marker='+', c=[colors[int(x) % len(colors)] for x in
            category.values], figsize=(18, 12))
    if save:
        name = 'scatmat_topics_{}-{}.jpg'.format(i * num_columns, (i + 1) *
            num_columns) + suffix
        plt.savefig(os.path.join(data_path, name + '.jpg'))
    if show:
        if block:
            plt.show()
        else:
            plt.show(block=False)