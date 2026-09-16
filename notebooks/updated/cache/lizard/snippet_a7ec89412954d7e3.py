def set_sitelink(self, site, title, badges=()):
    sitelink = {'site': site, 'title': title, 'badges': badges}
    self.wd_json_representation['sitelinks'][site] = sitelink
    self.sitelinks[site] = sitelink