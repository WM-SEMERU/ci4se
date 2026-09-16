def create_form(self, obj=None):
    kbtype = request.args['kbtype'] if 'kbtype' in request.args else 'w'
    if kbtype == KnwKB.KNWKB_TYPES['written_as']:
        self.form = WrittenAsKnowledgeForm
    elif kbtype == KnwKB.KNWKB_TYPES['dynamic']:
        self.form = DynamicKnowledgeForm
    else:
        self.form = TaxonomyKnowledgeForm
    form = self.form()
    form.kbtype.data = kbtype
    return form