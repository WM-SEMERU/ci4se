def data(self):
    d = {}
    self.token = ''
    try:
        d = self.viz.data
        self.token = d.get('token')
    except Exception as e:
        logging.exception(e)
        d['error'] = str(e)
    return {'datasource': self.datasource_name, 'description': self.
        description, 'description_markeddown': self.description_markeddown,
        'edit_url': self.edit_url, 'form_data': self.form_data, 'slice_id':
        self.id, 'slice_name': self.slice_name, 'slice_url': self.slice_url,
        'modified': self.modified(), 'changed_on_humanized': self.
        changed_on_humanized, 'changed_on': self.changed_on.isoformat()}