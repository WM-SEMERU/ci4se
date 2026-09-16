def create_project(self, key, name=None, assignee=None, type='Software',
    template_name=None):
    if assignee is None:
        assignee = self.current_user()
    if name is None:
        name = key
    possible_templates = ['Basic', 'JIRA Classic', 'JIRA Default Schemes',
        'Basic software development']
    if template_name is not None:
        possible_templates = [template_name]
    templates = self.templates()
    template_key = list(templates.values())[0][
        'projectTemplateModuleCompleteKey']
    for template_name, template_dic in templates.items():
        if template_name in possible_templates:
            template_key = template_dic['projectTemplateModuleCompleteKey']
            break
    payload = {'name': name, 'key': key, 'keyEdited': 'false',
        'projectTemplateWebItemKey': template_key,
        'projectTemplateModuleKey': template_key, 'lead': assignee}
    if self._version[0] > 6:
        payload['type'] = type
    headers = CaseInsensitiveDict({'Content-Type':
        'application/x-www-form-urlencoded'})
    url = self._options['server'] + '/rest/project-templates/latest/templates'
    r = self._session.post(url, data=payload, headers=headers)
    if r.status_code == 200:
        r_json = json_loads(r)
        return r_json
    f = tempfile.NamedTemporaryFile(suffix='.html', prefix=
        'python-jira-error-create-project-', delete=False)
    f.write(r.text)
    if self.logging:
        logging.error(
            'Unexpected result while running create project. Server response saved in %s for further investigation [HTTP response=%s].'
             % (f.name, r.status_code))
    return False