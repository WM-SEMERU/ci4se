def dl_full_file(url, save_file_name):
    response = requests.get(url)
    with open(save_file_name, 'wb') as writefile:
        writefile.write(response.content)
    return