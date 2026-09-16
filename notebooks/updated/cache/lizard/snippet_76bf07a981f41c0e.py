def download_file(url, filename=None, show_progress=draw_pbar):
    if filename is None:
        filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    size = int(r.headers['Content-Length'].strip())
    seen = 0
    show_progress(0, size)
    seen = 1024
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            seen += 1024
            show_progress(seen, size)
            if chunk:
                f.write(chunk)
                f.flush()
    return filename