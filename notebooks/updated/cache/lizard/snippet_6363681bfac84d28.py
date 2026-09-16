def main(to_dir, from_dir):
    num = copy_cwl_files(from_dir=from_dir, to_dir=to_dir)
    if num > 0:
        click.echo('Copied {} CWL files to "{}".'.format(num, to_dir))
    else:
        msg = 'No CWL files found in "{}". Copied 0 files'.format(from_dir)
        click.echo(msg)