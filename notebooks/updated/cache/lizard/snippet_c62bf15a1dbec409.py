def get_context_data(self, request, **kwargs):
    context = super(TableTab, self).get_context_data(request, **kwargs)
    self.load_table_data()
    for table_name, table in self._tables.items():
        if len(self.table_classes) == 1:
            context['table'] = table
        context['%s_table' % table_name] = table
    return context