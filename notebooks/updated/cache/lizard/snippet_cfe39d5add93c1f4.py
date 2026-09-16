def _write_symlink(self, zf, link_target, link_path):
    info = zipfile.ZipInfo()
    info.filename = link_path
    info.create_system = 3
    info.external_attr = 2716663808
    zf.writestr(info, link_target)