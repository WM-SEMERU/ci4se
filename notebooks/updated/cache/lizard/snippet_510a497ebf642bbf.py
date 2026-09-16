def generate_package(params):
    pkg_data = package.PackageData(params)
    pkg_tree = package.PackageTree(pkg_data)
    pkg_tree.generate()
    pkg_tree.move()
    VCS(os.path.join(pkg_tree.outdir, pkg_tree.name), pkg_tree.pkg_data)