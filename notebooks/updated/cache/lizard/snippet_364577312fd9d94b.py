def handle_special_journals(citation_elements, kbs):
    for el in citation_elements:
        if el['type'] == 'JOURNAL' and el['title'] in kbs['special_journals']:
            if re.match('\\d{1,2}$', el['volume']):
                if el['year'] == '' and re.match('(19|20)\\d{2}$', el['page']):
                    el['type'] = 'MISC'
                    el['misc_txt'] = '%s,%s,%s' % (el['title'], el['volume'
                        ], el['page'])
                el['volume'] = el['year'][-2:] + '%02d' % int(el['volume'])
            if el['page'].isdigit():
                el['page'] = '%03d' % int(el['page'])
    return citation_elements