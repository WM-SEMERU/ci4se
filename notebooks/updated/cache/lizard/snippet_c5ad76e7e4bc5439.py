def download(branch=None, buildMod=False):
    gradlew = './gradlew'
    if os.name == 'nt':
        gradlew = 'gradlew.bat'
    if branch is None:
        branch = malmo_version
    subprocess.check_call(['git', 'clone', '-b', branch,
        'https://github.com/Microsoft/malmo.git', malmo_install_dir])
    os.chdir(malmo_install_dir)
    os.chdir('Minecraft')
    try:
        pathlib.Path('src/main/resources/version.properties').write_text(
            'malmomod.version={}\n'.format(malmo_version))
        if buildMod:
            subprocess.check_call([gradlew, 'setupDecompWorkspace', 'build',
                'testClasses', '-x', 'test', '--stacktrace', '-Pversion={}'
                .format(malmo_version)])
        minecraft_dir = os.getcwd()
    finally:
        os.chdir('../..')
    if 'MALMO_XSD_PATH' not in os.environ:
        print(
            'Please make sure you set the MALMO_XSD_PATH environment variable to "{}/Schemas"!'
            .format(str(pathlib.Path(malmo_install_dir).absolute())))
    return minecraft_dir