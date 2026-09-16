def is_website_affected(self, website):
    if self.domain is None:
        return True
    if not self.include_subdomains:
        return self.domain in website['subdomains']
    else:
        dotted_domain = '.' + self.domain
        for subdomain in website['subdomains']:
            if subdomain == self.domain or subdomain.endswith(dotted_domain):
                return True
        return False