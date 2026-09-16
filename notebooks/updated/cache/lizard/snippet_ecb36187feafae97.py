def clan_badge_url(self):
    if self.clan_tag is None:
        return None
    url = self.raw_data.get('clan').get('badge').get('url')
    if not url:
        return None
    return 'http://api.cr-api.com' + url