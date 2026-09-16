def generate(env):
    doxyfile_scanner = env.Scanner(DoxySourceScan, 'DoxySourceScan',
        scan_check=DoxySourceScanCheck)
    import SCons.Builder
    doxyfile_builder = SCons.Builder.Builder(action=
        'cd ${SOURCE.dir}  &&  ${DOXYGEN} ${SOURCE.file}', emitter=
        DoxyEmitter, target_factory=env.fs.Entry, single_source=True,
        source_scanner=doxyfile_scanner)
    env.Append(BUILDERS={'Doxygen': doxyfile_builder})
    env.AppendUnique(DOXYGEN='doxygen')