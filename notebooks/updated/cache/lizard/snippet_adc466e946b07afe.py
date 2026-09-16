def render_template_directory(deck, arguments):
    output_directory = dir_name_from_title(deck.title)
    if os.path.exists(output_directory):
        if sys.stdout.isatty():
            if ask('%s already exists, shall I delete it?' %
                output_directory, arguments.get('--noinput')):
                shutil.rmtree(output_directory)
        else:
            shutil.rmtree(output_directory)
    template_directory_path = '%s/templates/%s' % (remarkable.__path__[0],
        deck.presentation_type)
    shutil.copytree(template_directory_path, output_directory)
    if os.path.exists('resources'):
        log.info('Copying resources')
        shutil.copytree('resources', '%s/resources' % output_directory)
    else:
        log.info('No resources to copy')
    template_filename = '%s/index.html' % deck.presentation_type
    html = render_template(template_filename, deck.json)
    index_filename = '%s/index.html' % output_directory
    write_file(index_filename, html)
    return output_directory