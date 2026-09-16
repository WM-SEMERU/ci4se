def create(client, name):
    from renku.models.datasets import Author
    with client.with_dataset(name=name) as dataset:
        click.echo('Creating a dataset ... ', nl=False)
        author = Author.from_git(client.repo)
        if author not in dataset.authors:
            dataset.authors.append(author)
    click.secho('OK', fg='green')