def on_valid_article_extracted(article):
    with open(__get_pretty_filepath(my_local_download_dir_article, article),
        'w') as outfile:
        if my_json_export_style == 0:
            json.dump(article.__dict__, outfile, default=str, separators=(
                ',', ':'))
        elif my_json_export_style == 1:
            json.dump(article.__dict__, outfile, default=str, indent=4,
                sort_keys=True)