def style_classpath(self, products, scheduler):
    classpath_entries = self._tool_classpath('scalastyle', products, scheduler)
    return [classpath_entry.path for classpath_entry in classpath_entries]