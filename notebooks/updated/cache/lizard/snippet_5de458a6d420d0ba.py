def readCommaList(fileList):
    names = fileList.split(',')
    fileList = []
    for item in names:
        fileList.append(item)
    return fileList