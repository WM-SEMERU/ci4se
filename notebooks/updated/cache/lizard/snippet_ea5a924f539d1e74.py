def ListOutputModules(self):
    table_view = views.ViewsFactory.GetTableView(self._views_format_type,
        column_names=['Name', 'Description'], title='Output Modules')
    for name, output_class in output_manager.OutputManager.GetOutputClasses():
        table_view.AddRow([name, output_class.DESCRIPTION])
    table_view.Write(self._output_writer)
    disabled_classes = list(output_manager.OutputManager.
        GetDisabledOutputClasses())
    if not disabled_classes:
        return
    table_view = views.ViewsFactory.GetTableView(self._views_format_type,
        column_names=['Name', 'Description'], title='Disabled Output Modules')
    for name, output_class in disabled_classes:
        table_view.AddRow([name, output_class.DESCRIPTION])
    table_view.Write(self._output_writer)