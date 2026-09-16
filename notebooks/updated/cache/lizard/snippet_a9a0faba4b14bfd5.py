def compile_theme(theme, target, *, zip_=False):
    from jinja2 import Environment, FileSystemLoader
    env = Environment(loader=FileSystemLoader(theme))
    env.compile_templates(target, zip='deflated' if zip_ else None)