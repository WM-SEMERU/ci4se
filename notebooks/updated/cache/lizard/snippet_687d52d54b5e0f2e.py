def main(flags):
    dl = SheetDownloader(flags)
    dl.init()
    for file_info in settings.GOOGLE_SHEET_SYNC['files']:
        print('Downloading {}'.format(file_info['path']))
        dl.download_sheet(file_info['path'], file_info['sheet'], file_info[
            'range'])