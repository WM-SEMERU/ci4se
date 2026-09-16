def compile_bundle_entry(self, spec, entry):
    modname, source, target, modpath = entry
    bundled_modpath = {modname: modpath}
    bundled_target = {modname: target}
    export_module_name = []
    if isfile(source):
        export_module_name.append(modname)
        copy_target = join(spec[BUILD_DIR], target)
        if not exists(dirname(copy_target)):
            makedirs(dirname(copy_target))
        shutil.copy(source, copy_target)
    elif isdir(source):
        copy_target = join(spec[BUILD_DIR], modname)
        shutil.copytree(source, copy_target)
    return bundled_modpath, bundled_target, export_module_name