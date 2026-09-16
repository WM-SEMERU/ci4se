def WriteToPath(obj, filepath):
    with io.open(filepath, mode='w', encoding='utf-8') as filedesc:
        WriteToFile(obj, filedesc)