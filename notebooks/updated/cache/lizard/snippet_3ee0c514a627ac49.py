def check_or_confirm_overwrite(file_name):
    try:
        with open(file_name) as fd:
            header = next(fd)
            if header.find(':sedge:') == -1:
                okay = ask_overwrite(file_name)
                if okay:
                    backup_file(file_name)
                else:
                    return False
    except FileNotFoundError:
        click.echo('{} not found'.format(file_name), err=True)
    except StopIteration as e:
        click.echo(repr(e), err=True)
    else:
        return True