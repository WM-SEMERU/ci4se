def create_default_layout(config):
    project_name = config.get('project_name')
    project_version = config.get('project_version')
    if not project_name or not project_version:
        error('setup-issue',
            '--project-name and --project-version must be specified')
    init_dir = config.get_path('init_dir')
    if not init_dir:
        init_dir = config.get_invoke_dir()
    elif os.path.exists(init_dir) and not os.path.isdir(init_dir):
        error('setup-issue', 
            'Init directory exists but is not a directory: %s' % init_dir)
    sitemap_path = check_path(init_dir, 'sitemap.txt')
    conf_path = check_path(init_dir, 'hotdoc.json')
    md_folder_path = check_path(init_dir, 'markdown_files')
    assets_folder_path = check_path(init_dir, 'assets')
    check_path(init_dir, 'built_doc')
    cat_path = os.path.join(assets_folder_path, 'cat.gif')
    os.makedirs(init_dir)
    os.makedirs(assets_folder_path)
    os.makedirs(md_folder_path)
    with open(sitemap_path, 'w') as _:
        _.write('index.md\n')
    with open(conf_path, 'w') as _:
        _.write(json.dumps({'project_name': project_name, 'project_version':
            project_version, 'sitemap': 'sitemap.txt', 'index': os.path.
            join('markdown_files', 'index.md'), 'output': 'built_doc',
            'extra_assets': ['assets']}, indent=4))
    with open(os.path.join(md_folder_path, 'index.md'), 'w') as _:
        _.write('# %s\n' % project_name.capitalize())
        try:
            get_cat(cat_path)
            _.write("\nIt's dangerous to go alone, take this\n")
            _.write('\n![](assets/cat.gif)')
        except:
            pass