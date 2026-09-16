def _get_zip_filename(self):
    date = datetime.datetime.now().strftime('%Y_%m_%d-%H%M%S')
    zip_file = 'filemail_transfer_{date}.zip'.format(date=date)
    return zip_file