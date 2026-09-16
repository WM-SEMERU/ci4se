def write_in_tmpfile(text, tmpfile):
    try:
        tmpfile.write(text)
    except TypeError:
        tmpfile.write(str.encode(text))
    except UnicodeEncodeError:
        tmpfile.write(text.encode('utf-8'))