def build_configuration_parameters(app):
    env = Environment(loader=FileSystemLoader('{0}/_data_templates'.format(
        BASEPATH)))
    template_file = env.get_template('configuration-parameters.j2')
    data = {}
    data['schema'] = Config.schema()
    rendered_template = template_file.render(**data)
    output_dir = '{0}/configuration/generated'.format(BASEPATH)
    with open('{}/parameters.rst'.format(output_dir), 'w') as f:
        f.write(rendered_template)