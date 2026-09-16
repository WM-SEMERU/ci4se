def get_sections(self, gradebook_id='', simple=False):
    params = dict(includeMembers='false')
    section_data = self.get('sections/{gradebookId}'.format(gradebookId=
        gradebook_id or self.gradebook_id), params=params)
    if simple:
        sections = self.unravel_sections(section_data['data'])
        return [{'SectionName': x['name']} for x in sections]
    return section_data['data']