def get_tag(self, version):
    for rel in self._repo.releases():
        if rel.tag_name == version:
            return rel.name, rel.html_url
    return None, None