def loadalldatas():
    dependency_order = ['common', 'profiles', 'blog', 'democomments']
    for app in dependency_order:
        project.recursive_load(os.path.join(paths.project_paths.manage_root,
            app))