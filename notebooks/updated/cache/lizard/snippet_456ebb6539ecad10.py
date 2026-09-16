def usage(title, message, tutorial_message, tutorial, css_path=CSS_PATH):
    env = Environment()
    env.loader = FileSystemLoader(osp.join(CONFDIR_PATH, 'templates'))
    usage = env.get_template('usage.html')
    return usage.render(css_path=css_path, title=title, intro_message=
        message, tutorial_message=tutorial_message, tutorial=tutorial)