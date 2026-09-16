def export_project(self):
    output = copy.deepcopy(self.generated_project)
    data_for_make = self.workspace.copy()
    self.exporter.process_data_for_makefile(data_for_make)
    output['path'], output['files']['makefile'] = self.gen_file_jinja(
        'makefile_gcc.tmpl', data_for_make, 'Makefile', data_for_make[
        'output_dir']['path'])
    expanded_dic = self.workspace.copy()
    expanded_dic['rel_path'] = data_for_make['output_dir']['rel_path']
    groups = self._get_groups(expanded_dic)
    expanded_dic['groups'] = {}
    for group in groups:
        expanded_dic['groups'][group] = []
    self._iterate(self.workspace, expanded_dic)
    project_path, output['files']['cproj'] = self.gen_file_jinja(
        'eclipse_makefile.cproject.tmpl', expanded_dic, '.cproject',
        data_for_make['output_dir']['path'])
    project_path, output['files']['proj_file'] = self.gen_file_jinja(
        'eclipse.project.tmpl', expanded_dic, '.project', data_for_make[
        'output_dir']['path'])
    return output