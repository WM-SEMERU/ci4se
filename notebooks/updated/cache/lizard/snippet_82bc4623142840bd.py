def _legacy_symbol_table(build_file_aliases):
    table = {alias: _make_target_adaptor(TargetAdaptor, target_type) for 
        alias, target_type in build_file_aliases.target_types.items()}
    for alias, factory in build_file_aliases.target_macro_factories.items():
        if len(factory.target_types) == 1:
            table[alias] = _make_target_adaptor(TargetAdaptor, tuple(
                factory.target_types)[0])
    table['python_library'] = _make_target_adaptor(PythonTargetAdaptor,
        PythonLibrary)
    table['jvm_app'] = _make_target_adaptor(AppAdaptor, JvmApp)
    table['jvm_binary'] = _make_target_adaptor(JvmBinaryAdaptor, JvmBinary)
    table['python_app'] = _make_target_adaptor(AppAdaptor, PythonApp)
    table['python_tests'] = _make_target_adaptor(PythonTestsAdaptor,
        PythonTests)
    table['python_binary'] = _make_target_adaptor(PythonBinaryAdaptor,
        PythonBinary)
    table['remote_sources'] = _make_target_adaptor(RemoteSourcesAdaptor,
        RemoteSources)
    table['page'] = _make_target_adaptor(PageAdaptor, Page)
    table['pants_plugin'] = PantsPluginAdaptor
    table['contrib_plugin'] = PantsPluginAdaptor
    return SymbolTable(table)