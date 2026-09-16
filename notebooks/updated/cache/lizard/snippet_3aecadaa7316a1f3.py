def download_data(dataset_name=None, prompt=prompt_stdin):
    dr = data_resources[dataset_name]
    if not authorize_download(dataset_name, prompt=prompt):
        raise Exception('Permission to download data set denied.')
    if 'suffices' in dr:
        for url, files, suffices in zip(dr['urls'], dr['files'], dr['suffices']
            ):
            for file, suffix in zip(files, suffices):
                download_url(url=os.path.join(url, file), dir_name=
                    data_path, store_directory=dataset_name, suffix=suffix)
    elif 'dirs' in dr:
        for url, dirs, files in zip(dr['urls'], dr['dirs'], dr['files']):
            for file, dir in zip(files, dirs):
                print(file, dir)
                download_url(url=os.path.join(url, dir, file), dir_name=
                    data_path, store_directory=os.path.join(dataset_name, dir))
    else:
        for url, files in zip(dr['urls'], dr['files']):
            for file in files:
                download_url(url=os.path.join(url, file), dir_name=
                    data_path, store_directory=dataset_name)
    return True