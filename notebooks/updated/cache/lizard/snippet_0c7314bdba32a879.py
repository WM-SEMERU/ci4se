def generate_handler_sourcepath(self, toolchain, spec, loaderplugin_sourcepath
    ):
    npm_pkg_name = (self.node_module_pkg_name if self.node_module_pkg_name else
        self.find_node_module_pkg_name(toolchain, spec))
    if not npm_pkg_name:
        cls = type(self)
        registry_name = getattr(self.registry, 'registry_name',
            '<invalid_registry/handler>')
        if cls is NPMLoaderPluginHandler:
            logger.error(
                "no npm package name specified or could be resolved for loaderplugin '%s' of registry '%s'; please subclass %s:%s such that the npm package name become specified"
                , self.name, registry_name, cls.__module__, cls.__name__)
        else:
            logger.error(
                "no npm package name specified or could be resolved for loaderplugin '%s' of registry '%s'; implementation of %s:%s may be at fault"
                , self.name, registry_name, cls.__module__, cls.__name__)
        return {}
    working_dir = spec.get(WORKING_DIR, None)
    if working_dir is None:
        logger.info(
            'attempting to derive working directory using %s, as the provided spec is missing working_dir'
            , toolchain)
        working_dir = toolchain.join_cwd()
    logger.debug("deriving npm loader plugin from '%s'", working_dir)
    target = locate_package_entry_file(working_dir, npm_pkg_name)
    if target:
        logger.debug('picked %r for loader plugin %r', target, self.name)
        result = super(NPMLoaderPluginHandler, self
            ).generate_handler_sourcepath(toolchain, spec,
            loaderplugin_sourcepath)
        result.update({self.name: target})
        return result
    if exists(join(working_dir, 'node_modules', npm_pkg_name, 'package.json')):
        logger.warning(
            "'package.json' for the npm package '%s' does not contain a valid entry point: sources required for loader plugin '%s' cannot be included automatically; the build process may fail"
            , npm_pkg_name, self.name)
    else:
        logger.warning(
            "could not locate 'package.json' for the npm package '%s' which was specified to contain the loader plugin '%s' in the current working directory '%s'; the missing package may be installed by running 'npm install %s' for the mean time as a workaround, though the package that owns that source file that has this requirement should declare an explicit dependency; the build process may fail"
            , npm_pkg_name, self.name, working_dir, npm_pkg_name)
    return {}