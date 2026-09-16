def create(output_dir):
    template_path = os.path.join(os.path.dirname(__file__), 'project_template')
    click.secho("Let's create a new component!", fg='green')
    name = click.prompt('What is the name of this component (ex. python-pip)?')
    click.secho('')
    click.secho(
        "We assume this will be pushed to GitHub and Docker Hub eventually, but these don't have to exist yet."
        , fg='green')
    repo_owner = click.prompt(
        'GitHub repo owner (i.e. your username or organization name)')
    repo_name = click.prompt('GitHub repo name', default=name)
    dockerhub_owner = click.prompt('Docker Hub repo owner', default=repo_owner)
    dockerhub_name = click.prompt('Docker Hub repo name', default=repo_name)
    license_owner = click.prompt(
        'Who should be the copyright owner on project?', default=repo_owner)
    extra_context = {'name': name, 'name_shields_io': name.replace('-',
        '--'), 'current_year': datetime.datetime.now().year,
        'dependencies_cli_version': __version__, 'repo_owner': repo_owner,
        'repo_name': repo_name, 'dockerhub_owner': dockerhub_owner,
        'dockerhub_name': dockerhub_name, 'license_owner': license_owner}
    project_dir = cookiecutter(template_path, no_input=True, extra_context=
        extra_context, output_dir=output_dir)
    click.secho('')
    click.secho(
        '{name} is ready to go, `cd {project_dir}` and try running `dependencies test`!'
        .format(name=name, project_dir=project_dir), fg='green')
    click.secho(
        'We started you out with a fully functioning component based in python.\n'
         +
        "Once you've got a handle on how it works then you can change it to whatever language you want."
        )