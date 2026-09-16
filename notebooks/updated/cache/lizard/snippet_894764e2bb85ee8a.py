def url_request(target_url, output_file):
    request = urllib.request.urlopen(target_url)
    with open(output_file, 'wb') as targets:
        total_length = int(request.headers.get('content-length'))
        with click.progressbar(length=total_length, label='Downloading files'
            ) as bar:
            while True:
                data = request.read(4096)
                if not data:
                    break
                targets.write(data)
                bar.update(len(data))