def get_file_mime_encoding(parts):
    for part in parts:
        for subpart in part.split(' '):
            if subpart.startswith('compressed-encoding='):
                mime = subpart.split('=')[1].strip()
                return Mime2Encoding.get(mime)
    return None