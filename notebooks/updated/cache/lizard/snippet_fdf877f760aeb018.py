def process(self, pq):
    if pq.query != '':
        postcode = address = city = ''
        postcode_matches = self.re_UK_postcode.findall(pq.query)
        if len(postcode_matches) > 0:
            postcode = postcode_matches[-1]
        query_parts = [part.strip() for part in pq.query.split(',')]
        if postcode is not '' and re.search(postcode, query_parts[0]):
            part_before_postcode = query_parts[0].split(postcode)[0].strip()
            if self.re_blank.search(part_before_postcode) is None:
                address = part_before_postcode
            else:
                address = query_parts[0]
        else:
            address = query_parts[0]
        for part in query_parts[1:]:
            part = part.strip()
            if postcode is not '' and re.search(postcode, part) is not None:
                part = part.replace(postcode, '').strip()
            if self.re_unit_numbered.search(part) is not None:
                address = self._comma_join(address, part)
            elif self.re_unit_not_numbered.search(part) is not None:
                address = self._comma_join(address, part)
            else:
                city = self._comma_join(city, part)
        pq.postal = pq.postal or postcode
        pq.address = pq.address or address
        pq.city = pq.city or city
    return pq