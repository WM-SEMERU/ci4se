def find_loci(self):
    session = OAuth1Session(self.consumer_key, self.consumer_secret,
        access_token=self.session_token, access_token_secret=self.
        session_secret)
    r = session.get(self.loci)
    if r.status_code == 200 or r.status_code == 201:
        if re.search('json', r.headers['content-type'], flags=0):
            decoded = r.json()
        else:
            decoded = r.text
        for locus in decoded['loci']:
            self.loci_url.append(locus)