def light_novels(self, language='English'):
    projects = []
    r = requests.get(self.api, params={'action': 'query', 'list':
        'categorymembers', 'cmtitle': 'Category:Light_novel_({})'.format(
        language.replace(' ', '_')), 'cmtype': 'page', 'cmlimit': '500',
        'format': 'json'}, headers=self.header)
    if r.status_code == 200:
        jsd = r.json()
        projects.append([(x['title'], x['pageid']) for x in jsd['query'][
            'categorymembers']])
        if 'query-continue' in jsd:
            while True:
                r = requests.get(self.api, params={'action': 'query',
                    'list': 'categorymembers', 'cmtitle':
                    'Category:Light_novel_({})'.format(language.replace(' ',
                    '_')), 'cmtype': 'page', 'cmlimit': '500', 'cmcontinue':
                    jsd['query-continue']['categorymembers']['cmcontinue'],
                    'format': 'json'}, headers=self.header)
                if r.status_code == 200:
                    jsd = r.json()
                    projects.append([(x['title'], x['pageid']) for x in jsd
                        ['query']['categorymembers']])
                    if 'query-continue' not in jsd:
                        break
                else:
                    break
    return projects[0]