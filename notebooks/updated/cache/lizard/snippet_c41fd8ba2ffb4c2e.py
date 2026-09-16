def jinja_env(template_path):
    fs_loader = FileSystemLoader(os.path.dirname(template_path))
    env = Environment(loader=fs_loader, autoescape=True, trim_blocks=True,
        lstrip_blocks=True)
    env.filters['b64encode'] = portable_b64encode
    env.filters['b64decode'] = f_b64decode
    return env