def stopContext(self, context):
    if self.clear_context['module'] and inspect.ismodule(context
        ) or self.clear_context['class'] and inspect.isclass(context):
        self.connection.drop_database(self.database_name)