def _make_compile_argv(self, compile_request):
    sources_minus_headers = list(self._iter_sources_minus_headers(
        compile_request))
    if len(sources_minus_headers) == 0:
        raise self._HeaderOnlyLibrary()
    compiler = compile_request.compiler
    compiler_options = compile_request.compiler_options
    buildroot = get_buildroot()
    argv = [compiler.exe_filename] + compiler.extra_args + ['-c', '-fPIC'
        ] + compiler_options + ['-I{}'.format(os.path.join(buildroot,
        inc_dir)) for inc_dir in compile_request.include_dirs] + [os.path.
        join(buildroot, src) for src in sources_minus_headers]
    self.context.log.info("selected compiler exe name: '{}'".format(
        compiler.exe_filename))
    self.context.log.debug('compile argv: {}'.format(argv))
    return argv