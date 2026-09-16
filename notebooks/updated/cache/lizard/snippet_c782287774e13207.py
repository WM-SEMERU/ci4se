def _fetch_itemslist(self, current_item):
    if current_item.is_root:
        html = requests.get(self.base_url).text
        soup = BeautifulSoup(html, 'html.parser')
        for item_html in soup.select('.row .col-md-6'):
            try:
                label = item_html.select_one('h2').text
            except Exception:
                continue
            yield API(label, blob=item_html)
    else:
        for resource in current_item.json['resource']:
            label = '{}, {}'.format(resource['title'], resource['summary'])
            yield SMHIDataset(label, blob=resource)