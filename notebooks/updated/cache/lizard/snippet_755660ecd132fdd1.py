def doc(self):
    from metapack import MetapackDoc
    t = self.get_resource().get_target()
    return MetapackDoc(t, package_url=self.package_url)