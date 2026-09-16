def check_dead_scopes(self):
    for scope in self.dead_scopes:
        export = isinstance(scope.get('__all__'), ExportBinding)
        if export:
            all = scope['__all__'].names()
            if not scope.importStarred and os.path.basename(self.filename
                ) != '__init__.py':
                undefined = set(all) - set(scope)
                for name in undefined:
                    self.report(messages.UndefinedExport, scope['__all__'].
                        source, name)
        else:
            all = []
        for importation in scope.values():
            if isinstance(importation, Importation
                ) and not importation.used and importation.name not in all:
                self.report(messages.UnusedImport, importation.source,
                    importation.name)