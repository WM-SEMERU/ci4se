def update_table(event):
    update_number = 0
    for update in event.get('updates', []):
        header = '======= Update #%s on %s =======' % (update_number, utils
            .clean_time(update.get('startDate')))
        click.secho(header, fg='green')
        update_number = update_number + 1
        text = update.get('contents')
        click.secho(utils.clean_splitlines(text))