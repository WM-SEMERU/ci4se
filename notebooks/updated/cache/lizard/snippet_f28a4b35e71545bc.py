def main(argv, version=DEFAULT_VERSION):
    tarball = download_setuptools()
    _install(tarball, _build_install_args(argv))