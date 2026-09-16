def infer_theme():
    themes = [os.path.basename(theme).replace('.less', '') for theme in
        glob('{0}/*.less'.format(styles_dir))]
    if os.path.exists(theme_name_file):
        with open(theme_name_file) as f:
            theme = f.readlines()[0]
        if theme not in themes:
            theme = 'default'
    else:
        theme = 'default'
    return theme