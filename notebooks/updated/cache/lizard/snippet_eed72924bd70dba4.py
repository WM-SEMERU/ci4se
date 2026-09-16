def create_module_file(app, env, package, module, dest, suffix, dryrun, force):
    logger.debug('Create module file: package %s, module %s', package, module)
    template_file = MODULE_TEMPLATE_NAME
    template = env.get_template(template_file)
    fn = makename(package, module)
    var = get_context(app, package, module, fn)
    var['ispkg'] = False
    rendered = template.render(var)
    write_file(app, makename(package, module), rendered, dest, suffix,
        dryrun, force)