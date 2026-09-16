def build_howto(request=None):
    how_tos = {}
    for app in settings.INSTALLED_APPS:
        mod = import_module(app)
        app_dir = os.path.dirname(mod.__file__)
        how_to_file = os.path.join(app_dir, 'how_to.md')
        if os.path.exists(how_to_file):
            contents = open(how_to_file).read()
            how_tos[app] = markdown.markdown(contents)
    return render(request, 'admin/how-to/index.html', {'how_tos': how_tos})