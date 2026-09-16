def title(self, title):
    title = " What's it like out side {0}? ".format(title)
    click.secho('{:=^62}'.format(title), fg=self.colors.WHITE)
    click.echo()