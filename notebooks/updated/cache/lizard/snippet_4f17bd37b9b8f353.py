def get_corresponding_author_info(self):
    resp = requests.get(self.scopus_url)
    from lxml import html
    parsed_doc = html.fromstring(resp.content)
    for div in parsed_doc.body.xpath('.//div'):
        for a in div.xpath('a'):
            if '/cdn-cgi/l/email-protection' not in a.get('href', ''):
                continue
            encoded_text = a.attrib['href'].replace(
                '/cdn-cgi/l/email-protection#', '')
            key = int(encoded_text[0:2], 16)
            email = ''.join([chr(int('0x{}'.format(x), 16) ^ key) for x in
                map(''.join, zip(*([iter(encoded_text[2:])] * 2)))])
            for aa in div.xpath('a'):
                if 'http://www.scopus.com/authid/detail.url' in aa.get('href',
                    ''):
                    scopus_url = aa.attrib['href']
                    name = aa.text
                else:
                    scopus_url, name = None, None
    return scopus_url, name, email