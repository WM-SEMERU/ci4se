def main():
    data = Common.open_file(F_INFO)
    config = Common.open_file(F_CONFIG)
    file_full_path = ''
    env = load_jinja2_env(config['p_template'])
    for index, page in data.iteritems():
        logging.info('Creating ' + index + ' page:')
        template = env.get_template(page['f_template'] + config[
            'f_template_ext'])
        for lang, content in page['content'].items():
            if lang == 'NaL':
                if page['f_directory'] != '':
                    Common.make_dir(config['p_build'] + page['f_directory'])
                file_full_path = config['p_build'] + page['f_directory'
                    ] + page['f_name'] + page['f_endtype']
            else:
                if page['f_directory'] != '':
                    Common.make_dir(config['p_build'] + lang + '/' + page[
                        'f_directory'])
                file_full_path = config['p_build'] + lang + '/' + page[
                    'f_directory'] + page['f_name'] + page['f_endtype']
            with open(file_full_path, 'w') as target_file:
                target_file.write(template.render(content))
        logging.info('Page ' + index + ' created.')