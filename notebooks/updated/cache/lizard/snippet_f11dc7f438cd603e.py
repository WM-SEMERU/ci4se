def _generate_download_google_link(link):
    if 'id=' not in link:
        split_link = link.split('/')
        file_id = split_link[-2]
    else:
        split_link = link.split('id=')
        file_id = split_link[-1]
    return 'https://drive.google.com/uc?export=download&id=' + file_id