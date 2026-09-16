def pull(client, revision, auto_login):
    registry_url = detect_registry_url(client, auto_login=auto_login)
    repo = client.repo
    sha = repo.rev_parse(revision).hexsha
    short_sha = repo.git.rev_parse(sha, short=7)
    image = '{registry}:{short_sha}'.format(registry=registry_url.image,
        short_sha=short_sha)
    result = subprocess.run(['docker', 'image', 'pull', image])
    if result.returncode != 0:
        raise click.ClickException(
            """The image "{image}" was not pulled.

Push the repository to the server or build the image manually:

	docker build -t {image} ."""
            .format(image=image))