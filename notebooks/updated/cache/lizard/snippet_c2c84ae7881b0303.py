def update_link_rewrite(self, old_rel, old_text, new_text, single_link=False):
    links = self.metadata.xpath('./links/link[@rel="{}" and text()="{}"]'.
        format(old_rel, old_text))
    if len(links) < 1:
        log.warning('No links with link/[@rel="{}"and text()="{}"]'.format(
            str(old_rel), str(old_text)))
        return False
    for link in links:
        link.text = new_text
        if single_link:
            break
    return True