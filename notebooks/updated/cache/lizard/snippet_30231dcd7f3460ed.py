def _dep_id(self, dependency):
    params = dict(sep=self.separator)
    if isinstance(dependency, JarDependency):
        params.update(org=dependency.org, name=dependency.name, rev=
            dependency.rev)
        is_internal_dep = False
    else:
        params.update(org='internal', name=dependency.id)
        is_internal_dep = True
    return ('{org}{sep}{name}{sep}{rev}' if params.get('rev') else
        '{org}{sep}{name}').format(**params), is_internal_dep