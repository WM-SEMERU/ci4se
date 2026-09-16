def bootstrap_c_source(scheduler_bindings_path, output_dir, module_name=
    NATIVE_ENGINE_MODULE):
    safe_mkdir(output_dir)
    with temporary_dir() as tempdir:
        temp_output_prefix = os.path.join(tempdir, module_name)
        real_output_prefix = os.path.join(output_dir, module_name)
        temp_c_file = '{}.c'.format(temp_output_prefix)
        if PY2:
            temp_c_file = temp_c_file.encode('utf-8')
        c_file = '{}.c'.format(real_output_prefix)
        env_script = '{}.cflags'.format(real_output_prefix)
        scheduler_bindings_content = read_file(scheduler_bindings_path)
        scheduler_bindings = _hackily_rewrite_scheduler_bindings(
            scheduler_bindings_content)
        ffibuilder = cffi.FFI()
        ffibuilder.cdef(scheduler_bindings)
        ffibuilder.cdef(_FFISpecification.format_cffi_externs())
        ffibuilder.set_source(module_name, scheduler_bindings)
        ffibuilder.emit_c_code(temp_c_file)
        file_content = read_file(temp_c_file)
        if CFFI_C_PATCH_BEFORE not in file_content:
            raise Exception(
                'The patch for the CFFI generated code will not apply cleanly.'
                )
        file_content = file_content.replace(CFFI_C_PATCH_BEFORE,
            CFFI_C_PATCH_AFTER)
        file_content = _hackily_recreate_includes_for_bindings(file_content)
    _replace_file(c_file, file_content)
    _replace_file(env_script, get_build_cflags())