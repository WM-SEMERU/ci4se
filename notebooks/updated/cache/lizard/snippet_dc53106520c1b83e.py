def delete_single(site, domain, delete_code=False, no_prompt=False):
    click.secho('Deleting installation "{sn}" hosted on the domain {dn}'.
        format(sn=site.name, dn=domain.name), fg='yellow', bold=True)
    if not no_prompt:
        if delete_code:
            warn_text = click.style(
                """WARNING! THIS WILL PERMANENTLY DELETE THIS SITE AND ALL OF THE ASSOCIATED PROJECT CODE FILES!
THIS MEANS ALL DATA FILES, INCLUDING ANY CREATED CUSTOM APPLICATIONS AND PLUGINS WILL BE PERMANENTLY AND IRREVOCABLY ERASED!"""
                , fg='red', bold=True)
            click.echo(warn_text)
            prompt_text = click.style(
                'In order to continue, please re-input the site name', fg=
                'white', bold=True)
            prompt = click.prompt(prompt_text)
            if prompt != site.name:
                click.secho(
                    'Site name did not match, site will not be deleted. Aborting.'
                    , fg='red', bold=True)
                raise click.Abort('Site name prompt did not match')
        else:
            prompt_text = click.style(
                'Are you sure you want to delete this site entry? Your project files will still be preserved.'
                , fg='white', bold=True)
            click.confirm(prompt_text, abort=True)
    site.delete()
    if delete_code:
        _remove_code(site)
    domain_sites = [ds for ds in domain.sites if ds.id != site.id]
    if not len(domain_sites):
        Session.delete(domain)
    Session.commit()
    click.secho('{sn} removed'.format(sn=site.name), fg='yellow', bold=True)
    FNULL = open(os.devnull, 'w')
    subprocess.check_call(['service', 'nginx', 'restart'], stdout=FNULL,
        stderr=subprocess.STDOUT)