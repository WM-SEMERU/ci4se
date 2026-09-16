def sort_js_files(js_files):
    modules = [f for f in js_files if f.endswith(MODULE_EXT)]
    mocks = [f for f in js_files if f.endswith(MOCK_EXT)]
    specs = [f for f in js_files if f.endswith(SPEC_EXT)]
    other_sources = [f for f in js_files if not f.endswith(MODULE_EXT) and 
        not f.endswith(MOCK_EXT) and not f.endswith(SPEC_EXT)]
    sources = modules + other_sources
    return sources, mocks, specs