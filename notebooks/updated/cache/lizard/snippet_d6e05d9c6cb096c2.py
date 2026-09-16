def fetch_csv_dataframe(download_url, filename=None, subdir=None, **
    pandas_kwargs):
    path = fetch_file(download_url=download_url, filename=filename,
        decompress=True, subdir=subdir)
    return pd.read_csv(path, **pandas_kwargs)