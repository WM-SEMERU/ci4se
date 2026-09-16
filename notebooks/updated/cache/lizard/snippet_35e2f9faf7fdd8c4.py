def fetch_data_table(api_key, show_progress, retries):
    for _ in range(retries):
        try:
            if show_progress:
                log.info('Downloading WIKI metadata.')
            metadata = pd.read_csv(format_metadata_url(api_key))
            table_url = metadata.loc[0, 'file.link']
            if show_progress:
                raw_file = download_with_progress(table_url, chunk_size=
                    ONE_MEGABYTE, label=
                    'Downloading WIKI Prices table from Quandl')
            else:
                raw_file = download_without_progress(table_url)
            return load_data_table(file=raw_file, index_col=None,
                show_progress=show_progress)
        except Exception:
            log.exception('Exception raised reading Quandl data. Retrying.')
    else:
        raise ValueError(
            'Failed to download Quandl data after %d attempts.' % retries)