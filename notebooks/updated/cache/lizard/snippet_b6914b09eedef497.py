def checksums(self, install):
    check_md5(pkg_checksum(install, self.repo), self.tmp_path + install)